
class IDSClass:
    # Iterative Deepening Search Method
    def IDSearch(self, graph, src, dst):
        # level ve count adlı iki değişken başlatılır. 
        # stack adlı bir liste, (şehir, yolu, maliyeti) üçlüsü içeren bir öğeyle başlatılır. 
        # visited adlı bir küme, zaten ziyaret edilmiş olan şehirleri içerir.
        level = 0
        count = 0
        stack = [(src, [src], 0)]
        visited = {src}
        cost = 0
        while True:
            # Her iterasyonda level arttırılır. 
            level += 1
            while stack:
                # Eğer count, belirli bir seviyeye (level) ulaşmamışsa,
                # bir DFS gerçekleştirilir.
                if count <= level:
                    # count sıfırlanır ve stackten bir öğe çıkarılır.
                    count = 0
                    (node, path, cost) = stack.pop()
                    # Eğer çıkarılan şehir hedef şehir ise,  
                    # bulunan yolu, ziyaret edilen şehirleri ve maliyeti geri döndürür.
                    for temp in graph[node].keys():
                        if temp == dst:
                            cost = sum(int(graph[path[i - 1]][path[i]]) for i in range(1, len(path)))
                            cost += int(graph[node][temp])
                            return path + [temp], visited, cost
                        # Eğer hedef şehir değilse ve henüz ziyaret edilmemişse, 
                        # şehir visited sözlüğüne eklenir ve stacke eklenir.
                        else:
                            if temp not in visited:
                                visited.add(temp)
                                count += 1
                                stack.append((temp, path + [temp], cost + graph[node][temp]))
                #Eğer count, belirli bir seviyeye (level) ulaşmışsa, 
                # bir BFS gerçekleştirilir.
                else:
                    q = stack
                    visited_bfs = {src}
                    while q:
                        (node, path, cost) = q.pop(0)
                        # Eğer çıkarılan şehir hedef şehir ise,  
                        # bulunan yolu, ziyaret edilen şehirleri ve maliyeti geri döndürür.
                        for temp in graph[node].keys():
                            if temp == dst:
                                cost = sum(int(graph[path[i - 1]][path[i]]) for i in range(1, len(path)))
                                cost += int(graph[node][temp])
                                return path + [temp], visited, cost
                            # Eğer hedef şehir değilse ve henüz ziyaret edilmemişse, 
                            # şehir visited sözlüğüne eklenir ve 
                            # BFS yolunu devam ettirmek için q listesine eklenir.
                            else:
                                if temp not in visited_bfs:
                                    visited_bfs.add(temp)
                                    q.append((temp, path + [temp], cost + graph[node][temp]))
                    break