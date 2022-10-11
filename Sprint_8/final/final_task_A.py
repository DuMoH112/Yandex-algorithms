# 71792573

"""
-- ПРИНЦИП РАБОТЫ --
    1. Распокуем строку по условию задачи.
    
        Вам даны строки в запакованном виде.
        Определим запакованную строку (ЗС) рекурсивно.
        Строка, состоящая только из строчных букв английского алфавита является ЗС.
        Если A и B —– корректные ЗС, то и AB является ЗС. Если A —– ЗС, а n — однозначное натуральное число,
        то n[A] тоже ЗС. При этом запись n[A] означает, что при распаковке строка A записывается подряд n раз.
        Найдите наибольший общий префикс распакованных строк и выведите его (в распакованном виде).
        
        Иными словами, пусть сложение —– это конкатенация двух строк,
        а умножение строки на число — повтор строки соответствующее число раз.
        Пусть функция f умеет принимать ЗС и распаковывать её.
        Если ЗС D имеет вид D=AB, где A и B тоже ЗС, то f(D) = f(A) + f(B). Если D=n[A], то f(D) = f(A) × n.

    2. Найдем наибольший общий префикс распакованных строк путём поиска общего префикса двух строк.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(n*m), где n - количество строк, m - длина самой большой строки.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(n*m), где n - количество строк, m - длина самой большой строки.
"""

from typing import List


def unpack(zip_str: str):
    if not zip_str:
        return ''

    multiply, symbol, result = [], [], []
    for char in zip_str:
        if char.isnumeric():
            multiply.append(int(char))
        elif char == '[':
            symbol.append([])
        elif char == ']':
            if len(symbol) == 1:
                result.append(''.join(symbol.pop()) * multiply.pop())
            else:
                previous = ''.join(symbol.pop())
                symbol[-1].append(previous * multiply.pop())
        elif len(symbol) == 0:
            result.append(char)
        else:
            symbol[-1].append(char)

    return ''.join(result)


def max_prefix(rows: List[str]):
    prefix = rows[0]
    for string in rows[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]

    return prefix


if __name__ == '__main__':
    cnt_str = int(input())
    rows = [unpack(input()) for _ in range(cnt_str)]
    print(max_prefix(rows))
