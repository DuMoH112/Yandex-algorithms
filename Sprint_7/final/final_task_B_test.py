import os
import sys

from final_task_B import is_same_amounts

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
    ], "answer": False}
]


if __name__ == '__main__':
    for idx, row_t in enumerate(praktikum_tests):
        n = int(row_t['test'][0])
        points = list(map(int, row_t['test'][1].split(' ')))

        test(is_same_amounts, idx, row_t['answer'], [points])
