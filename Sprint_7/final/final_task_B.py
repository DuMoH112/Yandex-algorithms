# 71071159

"""
-- ПРИНЦИП РАБОТЫ --
    Для разбиения множества чисел на два подмножества использовался псевдополиномиальный алгоритм.

    Подробное описание алгоритма - https://ru.wikipedia.org/wiki/Задача_разбиения_множества_чисел

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(n*s), где n - количество элементов массива, s - размер суммы.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(s), где s - размер суммы.
"""


def is_same_amounts(points):
    sum_points = sum(points)
    if sum_points % 2 != 0:
        return False

    half_sum = sum_points // 2
    P = [True] + [False] * half_sum
    for point in points:
        for j in range(half_sum, point - 1, -1):
            p1 = P[j - point]
            p2 = P[j]
            P[j] = p1 or p2
            if j == half_sum and P[j]:
                return True

    return P[-1]


if __name__ == '__main__':
    n = int(input())
    points = list(map(int, input().split(' ')))

    print(is_same_amounts(points))
