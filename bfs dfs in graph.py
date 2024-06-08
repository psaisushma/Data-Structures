class Graph:
    def __init__(self):
        self.graph = {}
    def addEdge(self, a, b):
        if a not in self.graph:
            self.graph[a] = [b]
        else:
            self.graph[a].append(b)
    def bfs(self):
        a = self.graph
        queue = [1]
        visited = set()
        visited.add(1)
        while queue:
            curr = queue.pop(0)
            print(curr, end=" ")
            for i in a.get(curr, []):
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
    def dfs(self):
        a = self.graph
        stack = [1]
        visited = set()
        visited.add(1)
        while stack:
            curr = stack.pop()
            print(curr, end=" ")
            for i in a.get(curr, []):
                if i not in visited:
                    visited.add(i)
                    stack.append(i)
g = Graph()
n = int(input("Enter n no of edges : "))
for i in range(n):
    a, b = map(int, input().split())
    g.addEdge(a, b)
print(g.graph)
g.dfs()
print()
g.bfs()