import os
import sys

from final_task_A import broken_search

sys.path.append(os.getcwd())
from tools import test

praktikum_tests = [
    {"test": [9, 5, [7, 12, 19, 21, 100, 101, 1, 4, 5]], "answer": 8},
    {"test": [7, 2, [4, 5, 6, 7, 8, 9, 1, 2]], "answer": 7},

    {"test": [2, 1, [1, 2, 3, 5]], "answer": 0},
    {"test": [9, 5, [19, 21, 100, 101, 1, 4, 5, 7, 12]], "answer": 6},

    {"test": [7, 6, [4, 5, 6, 7, 8, 9, 1, 2]], "answer": 2},
    {"test": [6, 6, [5, 6, 7, 8, 1, 2]], "answer": 1},
    
    
    {"test": [2, 1, [5, 1]], "answer": 1},
    {"test": [2, 1, [1]], "answer": 0},
    {"test": [2, 1, [3]], "answer": -1},
]


if __name__ == '__main__':
    for idx, row in enumerate(praktikum_tests):
        target = row['test'][1]
        nums = row['test'][2]

        test(broken_search, idx, row['answer'], [nums, target])
