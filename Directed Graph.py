class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    def print_adjacency_list(self):
        for node in self.graph:
            print(f"{node}: {', '.join(map(str, self.graph[node]))}")
n = int(input("Enter the number of edges: "))
g = Graph()
for i in range(n):
    u, v = map(int, input("Enter edge (u v): ").split(" "))
    g.add_edge(u, v)
g.print_adjacency_list()