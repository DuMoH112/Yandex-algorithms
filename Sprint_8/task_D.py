import os
import sys

sys.path.append(os.getcwd())
from tools import test


def max_prefix(rows):
    prefix = rows[0]
    for string in rows[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]

    return len(prefix)


def main():
    n = int(input())
    print(max_prefix([input() for _ in range(n)]))


tests = [
    {"test": [
        '3',
        'abacaba',
        'abudabi',
        'abcdefg',
    ], "answer": 2},
    {"test": [
        '2',
        'tutu',
        'kukuku',
    ], "answer": 0},
    {"test": [
        '3',
        'qwe',
        'qwerty',
        'qwerpy',
    ], "answer": 3},
    
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        test(max_prefix, idx, row['answer'], [row['test'][1:]])
