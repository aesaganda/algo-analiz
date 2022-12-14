# Python Program to detect cycle in an undirected graph
from collections import defaultdict

# This class represents a undirected
# graph using adjacency list representation


class Graph:

    def __init__(self, vertices):

        # Kenar sayisi
        self.V = vertices  # Kenar sayisi

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Grafa köşe ekleme
    def addEdge(self, v, w):

        # Add w to v_s list
        self.graph[v].append(w)

        # Add v to w_s list
        self.graph[w].append(v)

    # Cycle kontrolünün gerçekleştirilmesi
    def isCyclicUtil(self, v, visited, parent):

        # dolaşılan node işaretlendi
        visited[v] = True

        # komşuların kontrol edilmesi
        for i in self.graph[v]:

            # eğer komşu köse ziyaret edilmemişse oraya git
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True
            # Eğer parent olmayan kenar iki kez gezildiyse döngü var demektir
            elif parent != i:
                return True

        return False

    def isCyclic(self):

        # Mark all the vertices
        # as not visited
        visited = [False] * (self.V)

        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for i in range(self.V):

            # Don't recur for u if it
            # is already visited
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, -1)) == True:
                    return True

        return False

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order


# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 4)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")

g.topologicalSort()

g1 = Graph(7)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 4)
g1.addEdge(1, 6)
g1.addEdge(2, 5)
g1.addEdge(3, 5)
g1.addEdge(3, 6)
g1.addEdge(6, 4)

if g1.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")

g1.topologicalSort()