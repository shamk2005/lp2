# Single Source Shortest Path using Greedy Algorithm (Dijkstra Algorithm)

def dijkstra(graph, source, vertices):

    distance = [9999] * vertices
    visited = [False] * vertices

    distance[source] = 0

    for i in range(vertices):

        minimum = 9999
        u = -1

        for j in range(vertices):
            if not visited[j] and distance[j] < minimum:
                minimum = distance[j]
                u = j

        visited[u] = True

        for v in range(vertices):

            if graph[u][v] != 0 and not visited[v]:

                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    print("\nShortest distance from source vertex", source)

    for i in range(vertices):
        print("Vertex", i, "-> Distance =", distance[i])


# -------- MAIN PROGRAM --------

vertices = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(vertices):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source vertex: "))

dijkstra(graph, source, vertices)

#INPUT
#Enter number of vertices: 5
#Enter adjacency matrix:
#0 10 0 5 0
#10 0 1 2 0
#0 1 0 0 4
#5 2 0 0 2 
#0 0 4 2 0
#Enter source vertex: 0

