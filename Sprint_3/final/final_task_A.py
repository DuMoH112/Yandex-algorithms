# 69416837

"""
-- ПРИНЦИП РАБОТЫ --
Посик по массиву со сломанной сортировкой осуществляется бинарным поиском.

Я реализовал рекурсивный бинарный поиск по отсортированному массиву со смещением,
с корректировкой на смещение отсортированного массива.

Выделяется центральный элемент массива,
если слевой стороны находится отсортированная часть и искомый элемент находтся там,
то производится стандартный бинарный поиск,
иначе, если элемент находиться в части, где сортировка смещена,
то поиск производится с учётом того, что есть смещение элементов.

При отсутсвии искомого элемента в массиве возвращается -1

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
При поиске элемента массив каждую итерацию делится попалам

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Поиск в отсортированном массиве стоит O(log n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Поиск занимает O(log n) памяти, помимо самого массива
"""

def binary_search(arr: [int], x: int, left: int, right: int) -> int:
    if right <= left:
        return -1

    mid = (left + right) // 2
    start_val = arr[left]
    mid_val = arr[mid]
    end_val = arr[right-1]

    if arr[mid] == x:
        return mid
    elif start_val <= mid_val:
        if start_val <= x and x <= mid_val:
            return binary_search(arr, x, left, mid)
        else:
            return binary_search(arr, x, mid + 1, right)
    else:
        if mid_val <= x and x <= end_val:
            return binary_search(arr, x, mid + 1, right)
        else:
            return binary_search(arr, x, left, mid)


def broken_search(nums: [int], target: int) -> int:
    return binary_search(nums, target, 0, len(nums))
