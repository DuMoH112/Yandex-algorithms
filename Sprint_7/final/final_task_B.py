# 71103401

"""
-- ПРИНЦИП РАБОТЫ --
    Вдохновлялся статьёй: https://ru.wikipedia.org/wiki/Задача_разбиения_множества_чисел
    
        Для разбиения множества чисел на два подмножества использовался псевдополиномиальный алгоритм.

        Составим булеву матрицу P[K//2, n], где
            n - длина подмножества S,
            а K - сумма подмножества.        
        Первичным наполением матрицы будет значение False по всем ячейкам, кроме первой строки

        P(i, j) рассчитывается по формуле: P[i][j] = P[i][j-1] or P[i - S[j-1]][j-1]

        Пример матрицы:
        n = 3, points = {1, 3, 4}

          | { } | {1} | {1, 3} | {1, 3, 4}
        0 |  +  |  +  |    +   |     +     
        1 |  -  |  +  |    +   |     +    
        2 |  -  |  -  |    -   |     -     
        3 |  -  |  -  |    -   |    (+)     <- Это ответ на задачу

    Так как нам нужно сказать можно ли разбить множество S на два подмножества с одинаковой суммой,
    то нам достаточно хранить только последний столбец матрицы.


    Поэтому вместо матрицы будем составлять список P[K//2]
    Для удобства счёта добавим перед первым элементом True.    

    Наша матрица привратилась в массив. 
    [True, True, False, (True)]
                           ^
                           |
                  Это ответ на задачу
    
    Также будем проходить матрицу в обратном порядке,
    что поможет нам немного ускорить алгоритм

    Ранее мы считали
    for i in range(1, half_sum):
        for j in range(1, n):
            p = points[j-1]
            P[i][j] = P[i][j-1] or P[i - p][j-1]
    
    Теперь обходим так:
    for j in range(n):
        p = points[j]
        for i in range(half_sum, p-1, -1):
            P[j] = P[j] or P[j - p]

    

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(n*k), где n - количество элементов массива, k - размер суммы.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(k), где k - размер суммы.
"""


def is_same_amounts(points):
    sum_points = sum(points)
    if sum_points % 2 != 0:
        return False

    half_sum = sum_points // 2
    P = [True] + [False] * half_sum
    for p in points:
        for j in range(half_sum, p - 1, -1):
            P[j] = P[j] or P[j - p]
            if j == half_sum and P[j]:
                return True

    return P[-1]


def pseudopolynomial_time_algorithm(n, points):
    """
    Оригинальный алгоритм, с хранением полной матрицы
    """
    sum_points = sum(points)
    if sum_points % 2 != 0:
        return False

    half_sum = sum_points // 2
    P = [[False] * n for _ in range(half_sum)]
    P[0] = [True] * n
    for i in range(1, half_sum):
        for j in range(1, n):
            p = points[j-1]
            P[i][j] = P[i][j-1] or P[i - p][j-1]

    return P[-1][-1]


if __name__ == '__main__':
    n = int(input())
    points = list(map(int, input().split(' ')))

    print(is_same_amounts(points))
