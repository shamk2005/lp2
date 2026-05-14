import heapq

# Dijkstra's Algorithm
def dijkstra(graph, start):

    distances = {}

    for node in graph:
        distances[node] = float('inf')

    distances[start] = 0

    pq = [(0, start)]

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(pq, (distance, neighbor))

    return distances


# Main Program
n = int(input("Enter number of nodes: "))

graph = {}

for i in range(n):

    node = input("Enter node name: ")

    edges = int(input("Enter number of neighbors: "))

    graph[node] = []

    for j in range(edges):

        neighbor = input("Enter neighbor node: ")

        weight = int(input("Enter weight: "))

        graph[node].append((neighbor, weight))


start = input("Enter starting node: ")

distances = dijkstra(graph, start)

print("\nShortest distances from", start)

for node in distances:

    print(node, ":", distances[node])


#INPUT

=======
#Enter number of nodes: 4
#Enter node name: A
#Enter number of neighbors: 2
#Enter neighbor node: B
#Enter weight: 1
#Enter neighbor node: C
#Enter weight: 4
#Enter node name: B
#Enter number of neighbors: 2
#Enter neighbor node: C
#Enter weight: 2
#Enter neighbor node: D
#Enter weight: 5
#Enter node name: C
#Enter number of neighbors: 1
#Enter neighbor node: D
#Enter weight: 1
#Enter node name: D
#Enter number of neighbors: 0
#Enter starting node: A
