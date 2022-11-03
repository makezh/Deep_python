import numpy as np


# числа внутри матриц - рандом [0, 100]
def create_matrix(dim: (int, int)) -> np.array:
    matrix = np.random.randint(0, 100, dim)

    return matrix


# пусть матрицы будут квадратными
def chain_mul(count_of_matrix: int,
              dim: int) -> np.array:
    if count_of_matrix < 2:
        raise ValueError("count of matrices should be greater than 2")

    result = create_matrix((dim, dim))
    for _ in range(count_of_matrix - 1):
        new_matrix = create_matrix((dim, dim))
        result = result @ new_matrix

    return result


def main():
    if __name__ == "__main__":
        print(chain_mul(5, 3))
        return "end of main"

    return "just end"


main()
