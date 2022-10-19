import os
import sys

sys.path.append(os.getcwd())
from tools import test


def two_chips(numbers, X):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == X:
                return f"{numbers[i]} {numbers[j]}"

    return f"{None}"


def main():
    count_elements = int(input())
    numbers = [int(i) for i in input().split(' ')]
    X = int(input())
    print(two_chips(numbers, X))


def start_test():
    for idx, row in enumerate(tests):
        count_elements = int(row['test'][0])
        numbers = [int(i) for i in row['test'][1].split(' ')]
        X = int(row['test'][2])
        test(two_chips, idx, row['answer'], [numbers, X])


tests = [
    {"test": [
        "6",
        "-1 -1 -9 -7 3 -6",
        "2",
    ], "answer": "-1 3"},
    {"test": [
        "8",
        "6 2 8 -3 1 1 6 10",
        "100",
    ], "answer": "None"},
]

if __name__ == '__main__':
    start_test()
