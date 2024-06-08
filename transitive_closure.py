def transitive_closure(graph):
    V = len(graph)
    reach = []
    for i in range(V):
        row = []
        for j in range(V):
            row.append(graph[i][j])
        reach.append(row)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return reach

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

V = int(input("Enter the number of vertices: "))
graph = []
for i in range(V):
    row = list(map(int, input("Enter row {} of the adjacency matrix: ".format(i+1)).split()))
    graph.append(row)

closure = transitive_closure(graph)
print("Transitive closure of the given graph:")
print_matrix(closure)