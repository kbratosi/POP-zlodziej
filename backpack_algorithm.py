from pprint import pprint
import copy


class Field:
    def __init__(self):
        self.score = 0
        self.index_list = []

    def __repr__(self):
        return str(self.score)


A = [1, 2, 3, 4]
V = [4, 3, 2, 1]

W = 6

P = [[Field() for _ in range(W + 1)] for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, W + 1):
        if A[i - 1] > j:
            P[i][j] = copy.deepcopy(P[i - 1][j])
        else:
            skip_score = P[i - 1][j].score
            take_score = P[i - 1][j - A[i - 1]].score + V[i - 1]
            if take_score > skip_score:
                P[i][j].score = take_score
                P[i][j].index_list = copy.deepcopy(P[i - 1][j - A[i - 1]].index_list)
                P[i][j].index_list.append(i - 1)
            else:
                P[i][j] = copy.deepcopy(P[i - 1][j])

pprint(P)
print("Answer: {}".format(P[len(A)][W].index_list))
