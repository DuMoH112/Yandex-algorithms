# 71837353

"""
-- ПРИНЦИП РАБОТЫ --
    1.  Создадим префиксное дерево.
        В терминальные узлы будем записывать дополнительную информацию - длину слова.

    2.  Создадим массив с булевыми промежуточные значения - можно ли создать строку с данным индексом или же нет.
        Для каждого индекса будем проходить по префиксному дереву.
        Когда мы встречаем терминальный узел и при этом,
        ответ положительный и для строки без текущего рассматриваемого слова,
        тогда записываем в массив True.
        В противном случае записывается False.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(L) - построение префиксного дерева, где L — суммарная длина всех слов во множестве.
    O(n^2) - прохождение по префиксному дереву, где n - количество символов в строке.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(L) - префиксное дерево, где L — суммарная длина всех слов во множестве.
    O(n) - массив, где n - количество символов в строке.
"""

from typing import List


class Node:
    def __init__(self, value: str):
        self.value = value
        self.next = {}
        self.terminal = False


def create_tree(words: List[str]) -> Node:
    root = Node(None)
    for word in words:
        node = root
        for char in word:
            node.next[char] = node.next.get(char, Node(char))
            node = node.next[char]
        node.terminal = len(word)
    return root


def cheat_sheet(text: str, words: List[str]) -> str:
    root = create_tree(words)
    dp = [True] + [False] * len(text)
    for i in range(len(text)):
        node = root
        if dp[i]:
            for j in range(i, len(text) + 1):
                if node.terminal:
                    dp[j] = True
                if j == len(text) or not node.next.get(text[j], False):
                    break
                node = node.next[text[j]]

    return 'YES' if dp[-1] else 'NO'


if __name__ == '__main__':
    text = input()
    cnt_words = int(input())
    words = [input() for _ in range(cnt_words)]

    print(cheat_sheet(text, words))
