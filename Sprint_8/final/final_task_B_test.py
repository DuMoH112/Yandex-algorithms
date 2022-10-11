import os
import sys

from final_task_B import cheat_sheet

sys.path.append(os.getcwd())
from tools import test

praktikum_tests = [
    {"test": [
        'examiwillpasstheexam',
        '5',
        'will',
        'pass',
        'the',
        'exam',
        'i',
    ], "answer": "YES"},
    {"test": [
        'abacaba',
        '2',
        'abac',
        'caba',
    ], "answer": "NO"},
    {"test": [
        'abacaba',
        '3',
        'abac',
        'caba',
        'aba',
    ], "answer": "YES"},
    {"test": [
        'sscevscescescscsscevscevscesscsc',
        '4',
        'sce',
        's',
        'scev',
        'sc',
    ], "answer": "YES"},
        {"test": [
        'hfbfhfbfhfbfhhfbfhfbhfbhhhhfhfbf',
        '4',
        'hfb',
        'hf',
        'hfbf',
        'h',
    ], "answer": "YES"}
]


if __name__ == '__main__':
    for idx, row_t in enumerate(praktikum_tests):
        text = row_t['test'][0]
        cnt_words = int(row_t['test'][1])
        words = [w for w in row_t['test'][2:]]

        test(cheat_sheet, idx, row_t['answer'], [text, words])
