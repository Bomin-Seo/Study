import numpy as np

class Matrix:
    elem1, elem2, elem3, elem4 = 0, 0, 0, 0
    def __init__(self, num1, num2, num3, num4):
        self.elem1 = num1
        self.elem2 = num2
        self.elem3 = num3
        self.elem4 = num4

    def __add__(self, other):
        add_matrix = [[0, 0], [0, 0]]
        add_matrix = np.array(add_matrix)
        add_matrix[0][0] = self.elem1 + other.elem1
        add_matrix[0][1] = self.elem2 + other.elem2
        add_matrix[1][0] = self.elem3 + other.elem3
        add_matrix[1][1] = self.elem4 + other.elem4
        return add_matrix

    def __sub__(self, other):
        sub_matrix = [[0, 0], [0, 0]]
        sub_matrix = np.array(sub_matrix)
        sub_matrix[0][0] = self.elem1 - other.elem1
        sub_matrix[0][1] = self.elem2 - other.elem2
        sub_matrix[1][0] = self.elem3 - other.elem3
        sub_matrix[1][1] = self.elem4 - other.elem4
        return sub_matrix



if __name__ == "__main__":
    A = Matrix(1, 2, 3, 4)
    B = Matrix(5, 6, 7, 8)
    C = A+B
    D = A-B
    print(C)
    print(D)