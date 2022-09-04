# 69829861

"""
-- ПРИНЦИП РАБОТЫ --
    1.  Формируем из всего массива бинарную кучу.
        Для этого проходим справа-налево элементы (от последних к первым) и если у элемента есть потомки,
        то для него делаем просейку.
    
    2.  Максимумы ставим в конец неотсортированной части массива.
        Так как данные в массиве после первого этапа представляют из себя бинарную кучу,
        максимальный элемент находится на первом месте в массиве.
        Первый элемент (он же максимум) меняем с последним элементом неотсортированной части массива местами.
        После этого обмена максимум оказался своём окончательном месте, т.е. максимальный элемент отсортирован.
        Неотсортированная часть массива перестала быть бинарной кучей, но это исправляется однократной просейкой вниз —
        в результате чего на первом месте массива оказывается предыдущий по величине максимальный элемент.
        Действия этого этапа снова повторяются для оставшейся неупорядоченной области,
        до тех пор пока максимумы поочерёдно не будут перемещены на свои окончательные позиции.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    Сложности по времени зависит от просейки. Однократная просейка обходится в O(log(n)).

    1. Сначала для n элементов делаем просейку, чтобы из массива построить первоначальную кучу — O(nlog(n)).
    2. Далее, при вынесении n текущих максимумов из кучи, делаем однократную просейку
    для оставшейся неотсортированной части, этап также стоит O(nlog(n)).
    
    Итоговая сложность по времени: O(nlog(n)) + O(nlog(n)) = O(nlog(n)).

    При этом у пирамидальной сортировки нет ни вырожденных ни лучших случаев.
    Любой массив будет обработан на приличной скорости, но при этом не будет ни деградации ни рекордов.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Сложность по дополнительной памяти O(1).
    Сложность основной памяти O(n) для n элементов.
"""


class User:
    def __init__(self, name: str = None, solved_tasks: int = 0, fine: int = 0):
        self.name = name
        self.tasks = int(solved_tasks)
        self.fine = int(fine)

    def __gt__(self, other) -> bool:
        if self.tasks == other.tasks:
            if self.fine == other.fine:
                return self.name < other.name
            return self.fine < other.fine
        return self.tasks > other.tasks

    def __lt__(self, other) -> bool:
        if self.tasks == other.tasks:
            if self.fine == other.fine:
                return self.name > other.name
            return self.fine > other.fine
        return self.tasks < other.tasks

    def __str__(self):
        return self.name


class BinaryHeap:
    def __init__(self):
        self.heap = [None]
        self.size = 0

    def add(self, key: User) -> None:
        self.size += 1
        self.heap.append(key)
        self.sift_up(self.size)

    def pop(self) -> User:
        result = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.sift_down(1)
        return result

    def sift_up(self, index: int) -> None:
        if index == 1:
            return
        parent_index = index // 2

        if self.heap[parent_index] < self.heap[index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.sift_up(parent_index)

    def sift_down(self, index: int) -> int:
        left = 2 * index
        right = 2 * index + 1

        if self.size < left:
            return

        if (right <= self.size) and (self.heap[left] < self.heap[right]):
            index_largest = right
        else:
            index_largest = left

        if self.heap[index] < self.heap[index_largest]:
            self.heap[index], self.heap[index_largest] = self.heap[index_largest], self.heap[index]
            self.sift_down(index_largest)

    def __str__(self) -> str:
        return "\n".join(str(i) for i in self.heap[1:])


def heapsort(heap: BinaryHeap):
    sorted_array = []
    while heap.size > 0:
        sorted_array.append(str(heap.pop()))
        print(sorted_array[-1])
    
    return sorted_array


if __name__ == '__main__':
    cnt_users = int(input())
    heap = BinaryHeap()

    for _ in range(cnt_users):
        heap.add(User(*input().split(' ')))
    
    heapsort(heap)
