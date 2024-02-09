# math modülü, matematiksel işlemler için kullanılır.
import math
# RBFSClass sınıfı, Recursive Best-First Search (RBFS) algoritmasını uygulamak için kullanılır. 
# Sınıfın başlatıcı fonksiyonu, grafiği ve alternatif geçmiş listesini başlatır.
class RBFSClass:
    def __init__(self, graph):
        self.graph = graph
        self.alternative_global_history = [{'node': None, 'cost': float('inf')}]

    # RBFSSearch fonksiyonu, RBFS algoritmasının ana fonksiyonudur.
    # Başlangıç düğümü oluşturulur ve RBFS fonksiyonuna başlangıç düğümü, 
    # hedef düğüm, ve başlangıç için sonsuz maliyet limiti ile birlikte çağrılır.
    # Fonksiyon, bulunan yol ve maliyet limitini döndürür.
    def RBFSSearch(self, start, goal):
        start_node = {'state': start, 'parent': None, 'cost': 0, 'heuristic': self.heuristic(start, goal)}
        start_node['f'] = start_node['cost'] + start_node['heuristic']
        solution, f_limit = self.RBFS(self.graph, start_node, goal, float('inf'))
        return self.path(solution), f_limit

    # RBFS fonksiyonu, recursive best-first search algoritmasını uygular.
    # Eğer mevcut düğüm hedef düğüme eşitse, düğüm ve maliyet limiti döndürülür.
    # Komşu düğümler oluşturulur ve successors listesine eklenir.
    # Eğer successors boşsa, sonsuz maliyet ve maliyet limiti döndürülür.
    def RBFS(self, graph, node, goal, f_limit):
        if node['state'] == goal:
            return node, f_limit

        successors = []
        for neighbor, neighbor_cost in graph[node['state']].items():
            cost = neighbor_cost
            heuristic = self.heuristic(neighbor, goal)
            successor = {'state': neighbor, 'parent': node, 'cost': cost, 'heuristic': heuristic, 'f': cost + heuristic}
            successors.append(successor)

        if not successors:
            return {'f': float('inf')}, float('inf')  # İki değer döndürüyoruz

        # While döngüsü, successors listesi boş olana kadar devam eder.
        # Successors listesi maliyetlerine göre sıralanır ve en iyi (en düşük maliyetli) düğüm seçilir.
        while successors:
            successors.sort(key=lambda x: x['cost'])
            best = successors[0]
            d_best = best

            # Eğer en iyi düğüm hedefe ulaştı ve maliyet limitini aşmıyorsa, 
            # en iyi düğüm ve maliyet limiti döndürülür.
            # Eğer successors listesinde birden fazla düğüm varsa, 
            # alternatif maliyet ile global geçmişi güncellenir.
            if best['state'] == goal and best['cost'] <= f_limit:
                return best, f_limit
            
            if len(successors) > 1:
                alternative = successors[1]['cost']
                if alternative < self.alternative_global_history[-1]['cost']:
                    self.alternative_global_history.append({'node': successors[1], 'cost': alternative})
            
            # Eğer en iyi düğümün maliyeti, alternatif global geçmiş maliyetinden büyükse, 
            # en iyi düğümü alternatif ile değiştir.
            # Minimum komşu maliyet hesaplanır ve en iyi düğümün maliyetinden küçükse, 
            # en iyi düğümü alternatif ile değiştir.
            if best['cost'] > self.alternative_global_history[-1]['cost']:
                if self.alternative_global_history[-1]['node'] is not None and self.alternative_global_history[-1]['cost'] < best['cost']:
                    best = self.alternative_global_history[-1]['node']

                min_cost = min([graph[best['state']][neighbor] for neighbor in graph[best['state']]], default=float('inf'))
                if min_cost >= best['cost']:
                    best = d_best
                    alternative = self.alternative_global_history[-2]['cost']
                    if alternative == float('inf'):
                        alternative = self.alternative_global_history[-1]['cost']

            # Recursive çağrı yapılır ve sonuç ile yeni maliyet limiti alınır.
            # Eğer sonuç None değilse, sonuç ve maliyet limiti döndürülür.
            # En iyi düğüm successors listesinden çıkarılır.
            result, new_f_limit = self.RBFS(graph, best, goal, alternative)
            if result is not None:
                return result, new_f_limit
            successors.remove(best)
            
        return None, f_limit
    # Basit bir heuristic fonksiyonu, hedef düğüme olan maliyeti döndürür 
    # veya hedef düğüm yoksa 0 döndürür.
    def heuristic(self, node, goal):
        return self.graph[node][goal] if goal in self.graph[node] else 0

    # Yolu oluşturmak için kullanılan fonksiyon, 
    # mevcut düğüm ve ebeveynleri kullanarak yolu oluşturur.
    def path(self, node):
        if node is None or 'parent' not in node:
            return None
        path = []
        while node:
            path.append(node['state'])
            node = node['parent']
        return path[::-1]