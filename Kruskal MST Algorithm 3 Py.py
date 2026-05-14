# Kruskal's Minimum Spanning Tree Algorithm

class DisjointSet:

    def __init__(self, n):

        self.parent = list(range(n))

    # Find parent
    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # Union of sets
    def union(self, x, y):

        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False

        self.parent[yroot] = xroot

        return True


# Kruskal Algorithm
def kruskal_mst(edges, n):

    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(n)

    total_weight = 0

    print("\nEdges in MST:")

    for u, v, weight in edges:

        if ds.union(u, v):

            print(u, "-", v, ":", weight)

            total_weight += weight

    print("Total weight of MST:", total_weight)


# Main Program
n = int(input("Enter number of vertices: "))

e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")

for i in range(e):

    u, v, w = map(int, input().split())

    edges.append((u, v, w))

kruskal_mst(edges, n)


#INPUT

#Enter number of vertices: 4
#Enter number of edges: 5
#Enter edges (u v weight):
#0 1 10
#0 2 6
#0 3 5
#1 3 15
#2 3 4
