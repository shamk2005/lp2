# Minimum Spanning Tree using Greedy Algorithm (Prim's Algorithm)

def prims(graph, vertices):

    selected = [False] * vertices
    selected[0] = True

    edge_count = 0
    total_cost = 0

    print("\nEdge : Weight")

    while edge_count < vertices - 1:

        minimum = 9999
        x = 0
        y = 0

        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if (not selected[j]) and graph[i][j] != 0:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(x, "-", y, ":", graph[x][y])

        total_cost += graph[x][y]
        selected[y] = True
        edge_count += 1

    print("\nMinimum Cost =", total_cost)


# -------- MAIN PROGRAM --------

vertices = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix row by row:")

for i in range(vertices):
    row = list(map(int, input().split()))
    graph.append(row)

print("\nAdjacency Matrix:")
for row in graph:
    print(row)

prims(graph, vertices)



#OUTPUT
#Enter number of vertices: 4
#Enter adjacency matrix row by row:
#0 10 6 5 
#10 0 0 15
#6 0 0 4 
#5 15 4 0
