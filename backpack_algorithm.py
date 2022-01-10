from pprint import pprint
import copy


class Field:
    def __init__(self, score=0, index_list=[]):
        self.score = score
        self.index_list = index_list

    def __repr__(self):
        return str(self.score)

def backpack_algorithm(A, V, W):
    P = [[Field() for _ in range(W + 1)]]
    for _ in range(len(A)):
        P.append([Field()])

    for i in range(1, len(A) + 1):
        for j in range(1, W + 1):
            if A[i - 1] > j:
                P[i].append(copy.deepcopy(P[i - 1][j]))
            else:
                skip_score = P[i - 1][j].score
                take_score = P[i - 1][j - A[i - 1]].score + V[i - 1]
                if take_score > skip_score:
                    index_list = copy.deepcopy(P[i - 1][j - A[i - 1]].index_list)
                    index_list.append(i - 1)
                    P[i].append(Field(take_score, index_list))
                else:
                    P[i].append(copy.deepcopy(P[i - 1][j]))
    # convert answer to binary vector
    binary_vector = []
    for i in range(len(A)):
        if i in P[len(A)][W].index_list:
            binary_vector.append(1)
        else:
            binary_vector.append(0)
    return binary_vector, P[len(A)][W].score

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 7, 10, 2]
    V = [10, 8, 9, 4, 4, 13, 4, 9]
    W = 17

    answer, score = backpack_algorithm(A, V, W)
    print("score: {}, answer: {}".format(score, answer))