import numpy as np
import scipy as sc
import math


def matrix_multiplication(matrix_a, matrix_b):
    """
    Задание 1. Функция для перемножения матриц с помощью списков и циклов.
    Вернуть нужно матрицу в формате списка.
    """
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Multiplication is impossible due to different dimensions")
    
    result = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
    
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result


def functions(a_1, a_2):
    """
    Задание 2. На вход поступает две строки, содержащие коэффициенты двух функций.
    Необходимо найти точки экстремума функции и определить, есть ли у функций общие решения.
    Вернуть нужно координаты найденных решения списком, если они есть. None, если их бесконечно много.
    """

    # Функции имеют бесконечно много пересечений только в том случае, если они равны
    if a_1 == a_2:
        return None

    f = [list(map(float, a_1.split())), list(map(float, a_2.split()))]
    def F(x, k):
        return k[0]*x**2 + k[1]*x + k[2]

    # Определим разницу в коэффициентах двух функций
    a = f[0][0] - f[1][0]
    b = f[0][1] - f[1][1]
    c = f[0][2] - f[1][2]

    D = b**2 - 4*a*c

    result = []
    
    if a == 0: # не квадратная
        if b != 0: # ур-ние вида bx+c=0 => x=-c/b
            x = -c/b
            result.append((x, F(x, f[0])))
    else: # квадратная
        if D > 0:
            x_1 = (-b+math.sqrt(D)) / (2*a)
            x_2 = (-b-math.sqrt(D)) / (2*a)
            result.extend([(x_1, F(x_1, f[0])), (x_2, F(x_2, f[0]))])

    return result


def skew(x):
    """
    Задание 3. Функция для расчета коэффициента асимметрии.
    Необходимо вернуть значение коэффициента асимметрии, округленное до 2 знаков после запятой.
    """
    x = np.array(x)
    e = np.mean(x)

    third_central = np.sum((x-e)**3) / len(x)
    deviation = np.sum((x-e)**2) / len(x)
    asymmetry = third_central / (deviation ** 1.5) 

    return round(asymmetry, 2)

def kurtosis(x):
    """
    Задание 3. Функция для расчета коэффициента эксцесса.
    Необходимо вернуть значение коэффициента эксцесса, округленное до 2 знаков после запятой.
    """
    x = np.array(x)
    e = np.mean(x)

    fourth_central = np.sum((x-e)**4) / len(x)
    deviation = np.sum((x-e)**2) / len(x)
    excess = fourth_central / (deviation ** 2) - 3 

    return round(excess, 2)
