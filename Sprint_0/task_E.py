import os
import sys

sys.path.append(os.getcwd())
from tools import test


def two_chips_2(numbers, X):
    previous = set()
    for A in numbers:
        Y = X - A
        if Y in previous:
            return " ".join(str(i) for i in sorted([A, Y]))
        else:
            previous.add(A)

    return "None"


def main():
    count_elements = int(input())
    numbers = [int(i) for i in input().split(' ')]
    X = int(input())
    print(two_chips_2(numbers, X))


def start_test():
    for idx, row in enumerate(tests):
        count_elements = int(row['test'][0])
        numbers = [int(i) for i in row['test'][1].split(' ')]
        X = int(row['test'][2])
        test(two_chips_2, idx, row['answer'], [numbers, X])


tests = [
    {"test": [
        "6",
        "-9 -7 -6 -1 -1 3",
        "2",
    ], "answer": "-1 3"},
    {"test": [
        "8",
        "-3 1 1 2 6 6 8 10",
        "100",
    ], "answer": "None"},
]

if __name__ == '__main__':
    start_test()
