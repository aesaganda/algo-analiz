# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
# number of vertices in graph
V = 6


# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path


# Driver Code
if __name__ == "__main__":

    # matrix representation of graph
    graph = [[0, 2, 8, 15, 11, 6], [2, 0, 10, 9, 9, 4], [8, 10, 0, 7, 13, 14],
             [11, 9, 7, 0, 6, 11], [15, 9, 13, 6, 0, 5], [6, 4, 14, 11, 5, 0]]
    s = 0
    print("Toplam uzaklık:", travellingSalesmanProblem(graph, s))
