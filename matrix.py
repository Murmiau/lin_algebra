a = [[0, 1, 0], [2, 0, 1], [0, 0, 1]]
b = [[1, 2, 2], [0, 0, 1], [1, 0, 2]]

def matrix(a, b):
    try:
        matrix_AB = [[0 for _ in range(len(a))] for _ in range(len(b[0]))]
        for i in range(len(a)):
            for n in range(len(a[0])):
                for h in range(len(b[0])):
                    matrix_AB[i][h] = a[i][n] * b[n][h] + matrix_AB[i][h]
        print(*matrix_AB, sep="\n")
    except IndexError:
        print("Ошибка! Можно перемножить матрицы, у которых число столбцов первой матрицы, равно числу строк второй!")
matrix(a, b)
