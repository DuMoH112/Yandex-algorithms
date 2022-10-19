import os
import sys

sys.path.append(os.getcwd())
from tools import test


def zipper(count_elements, list_1, list_2):
    return " ".join([f"{list_1[i]} {list_2[i]}" for i in range(count_elements)])


def main():
    count_elements = int(input())
    list_1 = input().split(" ")
    list_2 = input().split(" ")
    print(zipper(count_elements, list_1, list_2))


def start_test():
    for idx, row in enumerate(tests):
        count_elements = int(row['test'][0])
        list_1 = row['test'][1].split(" ")
        list_2 = row['test'][2].split(" ")
        test(zipper, idx, row['answer'], [count_elements, list_1, list_2])


tests = [
    {"test": [
        "3",
        "1 2 3",
        "4 5 6",
    ], "answer": "1 4 2 5 3 6"},
    {"test": [
        "1",
        "1",
        "2",
    ], "answer": "1 2"},
    {"test": [
        "3",
        "1 8 9",
        "2 3 1",
    ], "answer": "1 2 8 3 9 1"},
]

if __name__ == '__main__':
    start_test()
