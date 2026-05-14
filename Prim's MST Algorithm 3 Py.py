import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for j in range(vertices)]
                      for i in range(vertices)]

    # Print MST
    def printMST(self, parent):

        print("\nEdge \tWeight")

        total = 0

        for i in range(1, self.V):

            weight = self.graph[parent[i]][i]

            print(parent[i] + 1, "-", i + 1, "\t", weight)

            total += weight

        print("Total weight of MST:", total)

    # Find minimum key vertex
    def minKey(self, key, mstSet):

        minimum = sys.maxsize

        for v in range(self.V):

            if key[v] < minimum and not mstSet[v]:

                minimum = key[v]
                min_index = v

        return min_index

    # Prim's Algorithm
    def primMST(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V

        key[0] = 0
        parent[0] = -1

        mstSet = [False] * self.V

        for _ in range(self.V):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):

                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:

                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


# Main Program
n = int(input("Enter number of vertices: "))

g = Graph(n)

print("Enter adjacency matrix:")

for i in range(n):

    row = list(map(int, input().split()))

    for j in range(n):

        g.graph[i][j] = row[j]

g.primMST()


#INPUT

#Enter number of vertices: 4
#Enter adjacency matrix:
#0 2 0 6 
#2 0 3 8
#0 3 0 0 
#6 8 0 0 
