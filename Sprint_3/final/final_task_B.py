# id package is 69445658

"""
-- ПРИНЦИП РАБОТЫ --
Сортировка массива осуществляется методом in-place quick sort.

При считывании данных я формирую массив объектов Person(отвечает за данные одной персоны).

Во время сортировки берётся крайний левый элемент массива, как опорный, и относительного него начинается упорядочивание массива.
Сначала должны идти элементы, не превосходящие опорного, а затем —– большие опорного.
Затем сортировка вызывается рекурсивно для двух полученных отрезков.

Наглядное изображение работы сортировки
https://contest.yandex.ru/testsys/statement-image?imageId=79587b4867d6af95afb4a295be8023fa21036db1cfa1b70b2768309a1fdb8ad4

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания алгоритма следует, что элементы должны отсортировываться относительно якорного элемента.
Таким образом, если взять точкой отсчёта первый элемент, то слева от него будут находиться значения, 
которые меют меньшее значение, а справа большее значение.

Алгоритм основан на подходе "разделяй-и-властвуй". Таким образовм мы разделям массив и влавствуем в каждом его диапазоне.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Хадшая стоимость алгоритма O(n^2)
Средняя стоимость O(nlog n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Поиск занимает O(n) памяти.
"""


class Person:
    def __init__(self, name, tasks, fine):
        self.name = name
        self.tasks = int(tasks)
        self.fine = int(fine)

    def __str__(self) -> str:
        return self.name

    def __gt__(self, other) -> bool:
        if self.tasks == other.tasks:
            if self.fine == other.fine:
                return self.name > other.name
            return self.fine > other.fine
        return self.tasks < other.tasks

    def __lt__(self, other) -> bool:
        if self.tasks == other.tasks:
            if self.fine == other.fine:
                return self.name < other.name
            return self.fine < other.fine
        return self.tasks > other.tasks


def quicksort(nums, left, right):
    if left >= right:
        return

    l, r = left, right
    pivot = nums[left]

    while l <= r:
        while nums[l] < pivot:
            l += 1
        while nums[r] > pivot:
            r -= 1

        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    quicksort(nums, left, r)
    quicksort(nums, l, right)


def main(cnt_students: str, students: [Person]):
    quicksort(students, 0, cnt_students - 1)
    print("\n".join([str(p) for p in students]))
    return [str(i.name) for i in students]


if __name__ == '__main__':
    cnt_students = int(input())
    students = [Person(*input().split(' ')) for l in range(cnt_students)]
    main(cnt_students, students)
