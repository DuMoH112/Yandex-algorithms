# 71893655

"""
-- ПРИНЦИП РАБОТЫ --
    1. Распокуем строку по условию задачи.
         Пусть функция f умеет принимать ЗС и распаковывать её.
         Если ЗС D имеет вид D=AB, где A и B тоже ЗС, то f(D) = f(A) + f(B). Если D=n[A], то f(D) = f(A) × n.

    2. Найдем наибольший общий префикс распакованных строк путём поиска общего префикса двух строк.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(n*m), где n - количество строк, m - длина самой большой строки.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(n*m), где n - количество строк, m - длина самой большой строки.
"""

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


def max_prefix(prefix: str, string: str):
    while string[:len(prefix)] != prefix and prefix:
        prefix = prefix[:-1]

    return prefix


if __name__ == '__main__':
    cnt_str = int(input())
    prefix = unpack(input())
    for _ in range(cnt_str-1):
        prefix = max_prefix(prefix, unpack(input()))
        
    print(prefix)
