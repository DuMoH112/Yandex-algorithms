import os
import sys

from final_task_B import main

sys.path.append(os.getcwd())
from tools import test

tests = [
    {
        "test": "3 4 +",
        "answer": "7"
    },
    {
        "test": "12 5 /",
        "answer": "2"
    },
    {
        "test": "10 2 4 * -",
        "answer": "2"
    },
    {
        "test": "2 1 + 3 *",
        "answer": "9"
    },
    {
        "test": "7 2 + 4 * 2 +",
        "answer": "38"
    },
    {
        "test": "2 4 + 4 6 + *",
        "answer": "60"
    },
    {
        "test": "2 1 2 / *",
        "answer": "0"
    },
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        test(main, idx, tests[idx]['answer'], [row['test']])
