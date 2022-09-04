# 69496053

"""
-- ПРИНЦИП РАБОТЫ --
Для хранения ключей и значений в HashTable я решил использовать массивы,
таким образом получу ассоциативный массив, при котором все данные записываются и хранятся в виде пар.

_hash функция реализует простой метод остатков.
Для разрешения коллизий используется _find_idx, реализовано линейное пробирование с повторным хэшированием.

Функция get:
    Вычисляется начальное хэш-значение, после чего начинается поиск соответсвующих значений в массиве _keys.
    Ищется до тех пор, пока не найдётся искомый key или не закончится массив.
    Если ничего не нашлось, то возвращается None.

Функция put:
    Вычисляется начальное хэш-значение и если по текущему адресу для данного key пустое значение, то туда записывается value,
    если по адресу key находится значение key и там лежит значени, то value перезаписывается. Иначе ищется пустой слот
    в массиве и значение записывается в пустой слот. Если непустой слот уже содержит key, то value перезаписывается.

Функция delete:
    Находится значение по ключу get(key),
    если value != None, то на место этого значения вставляется None.
    Возвращает найденое значение 

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Операция нахождения элемента занимает O(1) врмени.

В самом худшем случае может занять O(n). Свзяано это с тем, что
элементы внутри могут быть сдвинуты до самого конца массива, таким образом,
чтобы получить нужное нам значение придётся пройтись по всему массиву.

Но преапочтительно алгоритм занимает O(1) времени.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
HashTable занимает O(n) памяти
"""


class HashTable:
    def __init__(self, size):
        self._size = size
        self._keys = [None] * size
        self._values = [None] * size

    def get(self, key):
        idx = self._find_idx(self._hash(key), key)
        return self._values[idx] if self._keys[idx] == key else None

    def put(self, key, value):
        idx_key = self._hash(key)

        if self._keys[idx_key] is None:
            self._keys[idx_key] = key
            self._values[idx_key] = value
        elif self._keys[idx_key] == key:
            self._values[idx_key] = value
        else:
            next_idx_key = self._find_idx(self._hash(idx_key + 1), key)
            if self._keys[next_idx_key] is None:
                self._keys[next_idx_key] = key
                self._values[next_idx_key] = value
            else:
                self._values[next_idx_key] = value

    def delete(self, key):
        value = self.get(key)
        if value != None:
            self.put(key, None)
        return value

    def _hash(self, key):
        return hash(key) % self._size

    def _find_idx(self, idx, key):
        while self._keys[idx] is not None and self._keys[idx] != key:
            idx = self._hash(idx + 1)
        return idx


def performing_an_operation(ht: HashTable, cmd: [str], kv:[str]):
    if cmd == "get":
        print(ht.get(int(kv[0])))
    elif cmd == "put":
        ht.put(int(kv[0]), int(kv[1]))
    elif cmd == "delete":
        print(ht.delete(int(kv[0])))


if __name__ == '__main__':
    cnt_query = int(input())
    ht = HashTable(cnt_query)
    for _ in range(cnt_query):
        cmd, *kv = input().split(' ')
        performing_an_operation(ht, cmd, kv)
