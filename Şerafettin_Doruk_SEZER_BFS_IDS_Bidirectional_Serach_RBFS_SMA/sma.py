# heapq modülü, öncelikli kuyruk (priority queue) işlemleri için kullanılır.
import heapq
# SMAClass sınıfı, Simple Memory-Bounded A* (SMA*) algoritmasını uygulamak için kullanılır. 
# Sınıfın başlatıcı fonksiyonu, grafiği başlatır.
class SMAClass:
    def __init__(self, graph):
        self.graph = graph

    # SMASearch fonksiyonu, SMA* algoritmasının ana fonksiyonudur.
    # Başlangıç düğümü oluşturulur ve açık düğümler listesine eklenir.
    def SMASearch(self, start, goal, memory_limit=float('inf')):
        start_node = {'state': start, 'g': 0, 'h': self.heuristic(start, goal), 'parent': None}
        open_nodes = [start_node]
        closed_nodes = set()
        final_cost = None

        # While döngüsü, açık düğüm listesi boş olana kadar devam eder.
        # Her adımda, açık düğümler listesindeki en küçük f(n) değerine sahip düğüm seçilir 
        # ve bu düğüm açık düğümler listesinden kaldırılır.
        while open_nodes:
            current_node = min(open_nodes, key=lambda node: node['g'] + node['h']) # açık düğümler listesinden f(n) değeri en düşük olan düğümü seçer
            open_nodes.remove(current_node)
            current_state = current_node['state']
            current_g = current_node['g']

            # print(f"Current node: {current_state}")  # Current node print
            # Eğer mevcut düğüm hedef düğüme eşitse, hedefe ulaşılmış demektir. 
            # Fonksiyon, bulunan yolu ve toplam maliyeti döndürür.
            if current_state == goal:
                final_cost = current_g + self.heuristic(current_state, goal)
                return self.reconstruct_path(current_node), final_cost

            # Mevcut düğüm kapatılır ve komşuları değerlendirilir.
            closed_nodes.add(current_state)

            # Yeni düğüm oluşturulur ve açık düğüm listesi kontrol edilir. 
            # Eğer liste sınırlı bir bellek limitine ulaştıysa, 
            # en kötü düğüm (en yüksek toplam maliyetli) kaldırılır.
            # Eğer komşu düğüm açık düğüm listesinde yoksa, yeni düğüm listeye eklenir.
            # Eğer varsa ve mevcut maliyet daha düşükse, düğüm güncellenir.
            for neighbor, cost in self.graph[current_state].items():
                if neighbor not in closed_nodes:
                    new_g = current_g + cost # g(n)
                    new_node = {'state': neighbor, 'g': new_g, 'h': self.heuristic(neighbor, goal), 'parent': current_node} # h(n)

                    if len(open_nodes) > memory_limit:
                        worst_node = max(open_nodes, key=lambda node: node['g'] + node['h'])
                        open_nodes.remove(worst_node)

                        # En kötü düğümün çocuklarının maliyetlerini güncelle
                        for node in open_nodes:
                            if node['parent'] == worst_node:
                                node['g'] = float('inf')
                                node['parent'] = None
                        
                    
                    if not any(node['state'] == neighbor for node in open_nodes):
                        open_nodes.append(new_node)
                    else:
                        for node in open_nodes:
                            if node['state'] == neighbor and node['g'] > new_g:
                                node['g'] = new_g
                                node['parent'] = current_node
                                break

        # Eğer hedefe ulaşılamazsa, None ve final maliyet döndürülür.
        return None, final_cost
    
    # Basit bir heuristic fonksiyonu, hedef düğüme olan tahmini maliyeti döndürür.
    def heuristic(self, node, goal):
        for key in self.graph:
            if goal in self.graph[key]:
                return self.graph[key][goal]
        return float('inf')
    # Yolun yeniden oluşturulması fonksiyonu, bulunan yolu geriye doğru takip ederek bir liste oluşturur ve bu listeyi döndürür.
    def reconstruct_path(self, node):
        path = []
        while node is not None:
            path.append(node['state'])
            node = node['parent']
        return path[::-1]