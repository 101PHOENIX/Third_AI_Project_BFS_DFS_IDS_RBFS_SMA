class BidirectionalClass:
    def BidirectionalSearch(self, graph, start, goal):
        # Başlangıç ve hedefi takip eden iki ayrı explored listesi oluşturdum
        explored_start = set()
        explored_goal = set()

        # İki taraftan arama yapmak için iki ayrı frontier (sınır) listesi oluşturdum.
        frontier_start = [[start]]
        frontier_goal = [[goal]]

        # İki taraftan arama birleşene kadar devam eden bir döngü oluşturdum.
        while frontier_start and frontier_goal:
            # Başlangıç taraftan bir adım yapılır.
            path_start = frontier_start.pop(0)
            node_start = path_start[-1]

            # Hedef taraftan bir adım yapılır.
            path_goal = frontier_goal.pop(0)
            node_goal = path_goal[-1]
            
            
            # Eğer başlangıç taraftaki son şehir hedef tarafta zaten keşfedilmişse, birleşme noktası bulunmuştur.
            if node_start in explored_goal or node_goal in explored_start:
                # Toplam maliyeti hesaplamak için tüm adımlardaki kenar maliyetlerini topla
                total_cost = sum(graph[path_start[i]][path_start[i + 1]] for i in range(len(path_start) - 1))
                total_cost += sum(graph[path_goal[i]][path_goal[i + 1]] for i in range(len(path_goal) - 1))
                return path_start[::] + path_goal[::-1][1:], list(set(explored_start) | set(explored_goal)), total_cost

            # Eğer başlangıç taraftaki son şehir hedef tarafta keşfedilmemişse, devam edilir.
            for neighbor in graph[node_start]:
                if neighbor not in explored_start:
                    new_path = list(path_start)
                    new_path.append(neighbor)
                    frontier_start.append(new_path)
                    explored_start.add(neighbor)

            # Eğer hedef taraftaki son şehir başlangıç tarafta keşfedilmemişse, devam edilir.
            for neighbor in graph[node_goal]:
                if neighbor not in explored_goal:
                    new_path = list(path_goal)
                    new_path.append(neighbor)
                    frontier_goal.append(new_path)
                    explored_goal.add(neighbor)

        # İki taraftan yapılan arama birleşme noktasına ulaşamazsa, yol bulunamamıştır.
        print(f'No path exists between {start} and {goal}')