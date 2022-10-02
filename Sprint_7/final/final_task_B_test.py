import os
import sys

from final_task_B import is_same_amounts, pseudopolynomial_time_algorithm

sys.path.append(os.getcwd())
from tools import test

praktikum_tests = [
    {"test": [
        '4',
        '1 5 7 1',
    ], "answer": True},
    {"test": [
        '3',
        '2 10 9',
    ], "answer": False},
    {"test": [
        '3',
        '1 3 4',
    ], "answer": True},
    {"test": [
        '9',
        '9 8 7 6 5 4 3 2',
    ], "answer": True},
    {"test": [
        '2',
        '1 9',
    ], "answer": False},
    {"test": [
        '8',
        '11 11 9 9 5 5 1 1',
    ], "answer": True},
]


if __name__ == '__main__':
    for idx, row_t in enumerate(praktikum_tests):
        n = int(row_t['test'][0])
        points = list(map(int, row_t['test'][1].split(' ')))

        test(is_same_amounts, idx, row_t['answer'], [points])
        # test(pseudopolynomial_time_algorithm, idx, row_t['answer'], [n, points])
