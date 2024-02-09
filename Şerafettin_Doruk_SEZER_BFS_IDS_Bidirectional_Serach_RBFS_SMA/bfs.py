
class BFSClass:
    # BFS kullanarak bir grafiğin 2 düğümü arasındaki en kısa yolu bulma.
    def BFSearch(self,graph, start, goal):
        # ziyaret edilen şehirleri takip etmek için oluşturulur.
        explored = []
        # frontier adlı bir liste, kontrol edilecek tüm yolları takip etmek için oluşturulur. 
        # İlk olarak, başlangıç şehiri ile başlayan bir yol eklenir.
        frontier = [[start]]
        #  arama maliyetini takip etmek için oluşturulur 
        cost = 0

        # Başlangıç şehiri zaten hedef şehir ise, 
        # "You are already in Bucharest!" mesajıyla birlikte fonksiyonun çalışması sona erdirilir.
        if start == goal:
            return "You are already in Bucharest!"

        # while frontier: döngüsü, tüm olası yollar kontrol edilene kadar devam eder.
        while frontier:
            # Döngü içinde, frontier'dan ilk yolu çıkarır (FIFO) 
            # ve bu yolun sonundaki şehiri alır.
            path = frontier.pop(0)
            node = path[-1]
            #Eğer bu şehir daha önce ziyaret edilmediyse, 
            # maliyeti artırır ve komşu şehirleri kontrol eder.
            if node not in explored:
                neighbors = graph[node]
                # Her bir komşu şehir için, yeni bir yol oluşturur ve 
                # bu yolu frontier'a ekler. 
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    frontier.append(new_path)
                    
                    # Eğer komşu şehir hedef şehir ise, fonksiyon çalışmayı sonlandırır.
                    if neighbor == goal:
                        cost += sum(int(graph[new_path[i - 1]][new_path[i]]) for i in range(1, len(new_path)))
                        explored.append(goal)
                        return new_path, explored, cost

                # Ziyaret edilen şehir listesine mevcut şehiri ekler.
                explored.append(node)

        # Eğer iki şehir arasında bir bağlantı yoksa, 
        # "Connecting path doesn't exist" mesajıyla birlikte fonksiyon sona erdiriyor..
        return "Connecting path doesn't exist"
