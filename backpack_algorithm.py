from pprint import pprint

A = [1, 2, 3, 4]
V = [4, 3, 2, 6]

W = 6

P = [[0 for _ in range(W + 1)] for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(W + 1):
        if A[i - 1] > j:
            P[i][j] = P[i - 1][j]
        else:
            P[i][j] = max(P[i - 1][j], P[i - 1][j - A[i - 1]] + V[i - 1])

pprint(P)
