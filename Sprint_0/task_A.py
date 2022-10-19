import os
import sys

sys.path.append(os.getcwd())
from tools import test


def summa(a, b):
    return a + b


def main():
    print(summa(int(input()), int(input())))


def start_test():
    for idx, row in enumerate(tests):
        test(summa, idx, row['answer'], [
             int(row['test'][0]), int(row['test'][1])])


tests = [
    {"test": ['12', '90'], "answer": 102},
    {"test": ['200', '-200'], "answer": 0},
    {"test": ['1000000000', '1000000000'], "answer": 2000000000},
]

if __name__ == '__main__':
    start_test()
