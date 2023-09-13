# Напишите функцию для транспонирования матрицы.


def matrix_transposition(matrix):
    return list(list(i) for i in zip(*matrix))


MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f'Исходная матрица = {MATRIX = }')
print(f'Транспонированная матрица = {matrix_transposition(MATRIX)}')
