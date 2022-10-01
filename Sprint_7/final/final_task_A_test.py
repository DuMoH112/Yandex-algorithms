import os
import sys

from final_task_A import levenshtein_distance

sys.path.append(os.getcwd())
from tools import test

praktikum_tests = [
    {"test": [
        'abacaba',
        'abaabc',
    ], "answer": 2},
    {"test": [
        'innokentiy',
        'innnokkentia',
    ], "answer": 3},
    {"test": [
        'r',
        'x',
    ], "answer": 1},
]


if __name__ == '__main__':
    for idx, row_t in enumerate(praktikum_tests):
        str1 = row_t['test'][0]
        str2 = row_t['test'][1]

        test(levenshtein_distance, idx, row_t['answer'], [str1, str2])
