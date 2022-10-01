# 71068783

"""
Вдохновлялся статьёй: https://habr.com/ru/post/676858/

-- ПРИНЦИП РАБОТЫ --
    Для поиска расстояния Левенштейна будем использовать алгоритм Вагнера — Фишера.

    Составим матрицу D:
       D(i, j) растчитываeтся по формуле:
        Для i=0, j=0: 0
        Для i=0, j>0: j
        Для i>0, j=0: i
        Для i>0, j>0: min(D(i, j-1) + 1, D(i-1, j) + 1, D(i-1, j-1) + f(str1[i], str2[j])),
            где f(str1[i], str2[j]) - это сравнение символов на равенство, результатом будет 1 или 0.
        
    Для поиска расстояния Левенштейна нам необязательно хранить всю матрицу,
    достаточко только текущую строку в матрице и предыдущую.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(n*m), где n и m - длины строк

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(n), где n - длина наименьшей строки.
"""

def levenshtein_distance(str1: str, str2: str):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n
    
    cur_row = range(n + 1)
    for i in range(1, m + 1):
        prev_row, cur_row = cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1]
            if str1[j - 1] != str2[i - 1]:
                change += 1
            cur_row[j] = min(add, delete, change)

    return cur_row[n]


if __name__ == '__main__':
    str1 = input()
    str2 = input()

    print(levenshtein_distance(str1, str2))
