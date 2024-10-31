import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}
    def add_edge(self, vertex1, vertex2, weight=None, directed=False):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1][vertex2] = weight
        if not directed:
            self.graph[vertex2][vertex1] = weight

    def dijkstra(self, start):
            distances = {vertex: float('infinity') for vertex in self.graph}
            distances[start] = 0
            queue = [(0, start)]
            while queue:
                current_distance, current_vertex = heapq.heappop(queue)
                if current_distance > distances[current_vertex]:
                    continue
                for neighbor, weight in self.graph[current_vertex].items():
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(queue, (distance, neighbor))
            return distances


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 4)

start_vertex = 'A'
distances = g.dijkstra(start_vertex)
print("Distancias mínimas desde el vértice", start_vertex + ":")
for vertex, distance in distances.items():
    print("Distancia al vértice", vertex + ":", distance)