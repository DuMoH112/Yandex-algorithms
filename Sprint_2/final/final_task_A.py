# id package is 69333929

"""
-- ПРИНЦИП РАБОТЫ --
Дек представляет из себя очередь элементов,
в которой добавление новых элементов и удаление существующих производится с обоих концов структуры.

Я реализовал дек с использованием очереди на кольцевом буфере.
В деке хвост всегда указывает на первую свободную для записи ячейку,
а голова — на элемент, добавленный в начало структуры.

Если на момент извлечения дек пуст, или при добавлении нового элемента дек переполнен, то возвращается 
сообщение об ошибке вида 'error'.

Принцип работы очереди на кольцевом буфере представлен на этих изоображениях:
https://pictures.s3.yandex.net/resources/refactoring_01-3_1607336564.png
https://pictures.s3.yandex.net/resources/refactoring_01-2_1607336630.png

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания алгоритма следует, что чем раньше элемент добавился в дек, то
он может быть раньше из неё извлечен или будет извлечён последним.

Дек хранит элементы в том порядке, в каком они были добавлены
и может извлекать элементы с обоих концов структуры.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление в дек стоит O(1), когда дек не переполнен.
Извлечение из дека стоит O(1), когда дек не пуст.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Дек, содержащий n элементов, занимает O(n) памяти.
"""


class Deque:
    def __init__(self, len_deq: int):
        self.items = [None] * len_deq
        self.max_size = len_deq
        self.size = 0
        self.head = 0
        self.tail = 0
    
    def push_back(self, item: int):
        if self.size == self.max_size:
            raise IndexError

        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, item: int):
        if self.size == self.max_size:
            raise IndexError

        self.items[self.head - 1] = item
        self.head = (self.head - 1) % self.max_size
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError

        self.tail = (self.tail - 1) % self.max_size
        item = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1
        return item

    def pop_front(self):
        if self.size == 0:
            raise IndexError

        item = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item


def main(len_deq: int, cnt_command: int):
    d = Deque(len_deq)
    for i in range(cnt_command):
        com = input().split(' ')
        func, *item = com
        if item:
            item = int(item[0])

        res = None
        try:
            if func == "push_back":
                res = d.push_back(item)
            elif func == "push_front":
                res = d.push_front(item)
            elif func == "pop_back":
                res = d.pop_back()
            elif func == "pop_front":
                res = d.pop_front()
        except IndexError as e:
            res = 'error'
        
        if res != None:
            print(res)



if __name__ == '__main__':
    cnt_command = int(input())
    len_deq = int(input())

    main(len_deq, cnt_command)
