class Field:
    """Klasa przechowująca wynik rozwiązania cząstkowego oraz referencję na poprzednika"""

    def __init__(self, index, score=0, prev_field=None):
        self.score = score
        self.index = index
        self.prev_field = prev_field

    def __repr__(self):
        return str(self.index)


def backpack_algorithm(A, V, W):
    P = [[Field(index) for _ in range(W + 1)] for index in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, W + 1):
            if A[i - 1] > j:
                P[i][j] = P[i - 1][j]
            else:
                skip_score = P[i - 1][j].score
                take_score = P[i - 1][j - A[i - 1]].score + V[i - 1]
                if take_score > skip_score:
                    P[i][j].score = take_score
                    P[i][j].prev_field = P[i - 1][j - A[i - 1]]
                else:
                    P[i][j] = P[i - 1][j]

    index_list = []
    curr_field = P[len(A)][W]
    while curr_field.prev_field is not None:
        index_list.append(curr_field.index - 1)
        curr_field = curr_field.prev_field
    index_list.reverse()

    # Konwersja wyniku na wektor binarny
    binary_vector = []
    final_weight = 0
    for i in range(len(A)):
        if i in index_list:
            binary_vector.append(1)
            final_weight += A[i]
        else:
            binary_vector.append(0)
    return binary_vector, P[len(A)][W].score, final_weight


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 7, 10, 2]
    V = [10, 8, 9, 4, 4, 13, 4, 9]
    W = 17

    answer, score, weight = backpack_algorithm(A, V, W)
    print("score: {}, answer: {}, weight: {}".format(score, answer, weight))
