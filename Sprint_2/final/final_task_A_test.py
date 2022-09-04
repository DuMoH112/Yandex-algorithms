import os
import sys

from final_task_A import main

sys.path.append(os.getcwd())
from tools import test

tests = [
    {"test": [
        "8",
        "4",
        "push_front -201",
        "push_front -202",
        "push_front -203",
        "push_front -204",
        "pop_back",
        "pop_back",
        "pop_back",
        "pop_back",
    ], "answer": [
        "-201",
        "-202",
        "-203",
        "-204",
    ]},
    {"test": [
        "4",
        "4",
        "push_front 861",
        "push_front -819",
        "pop_back",
        "pop_back",
    ], "answer": [
        "861",
        "-819",
    ]},
    {"test": [
        "7",
        "10",
        "push_front -855",
        "push_front 0",
        "pop_back",
        "pop_back",
        "push_back 844",
        "pop_back",
        "push_back 823",
    ], "answer": [
        "-855",
        "0",
        "844",
    ]},
    {"test": [
        "6",
        "6",
        "push_front -201",
        "push_back 959",
        "push_back 102",
        "push_front 20",
        "pop_front",
        "pop_back",
    ], "answer": [
        "20",
        "102",
    ]},
    {"test": [
        "6",
        "2",
        "push_front -201",
        "push_back 959",
        "push_back 102",
        "push_front 20",
        "pop_front",
        "pop_back",
    ], "answer": [
        "error",
        "error",
        "-201",
        "959",
    ]},
]

if __name__ == '__main__':
    cnt_command, len_deq, commands = None, None, None
    for idx, row in enumerate(tests):
        cnt_command = int(row['test'][0])
        len_deq = int(row['test'][1])

        test(main, idx, row['answer'], [len_deq, cnt_command])
