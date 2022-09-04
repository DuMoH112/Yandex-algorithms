import os
import sys
import time

from final_task_A import heapsort, User, BinaryHeap

sys.path.append(os.getcwd())
from tools import test

praktikum_tests = [
    {"test": [
        "5",
        "alla 4 100",
        "gena 6 1000",
        "gosha 2 90",
        "rita 2 90",
        "timofey 4 80",
    ], "answer": [
        "gena",
        "timofey",
        "alla",
        "gosha",
        "rita",
    ]},
    {"test": [
        "5",
        "alla 0 0",
        "gena 0 0",
        "gosha 0 0",
        "rita 0 0",
        "timofey 0 0",
    ], "answer": [
        "alla",
        "gena",
        "gosha",
        "rita",
        "timofey",
    ]},
]


if __name__ == '__main__':
    for idx, row_t in enumerate(praktikum_tests):
        cnt_users = int(row_t['test'][0])
        heap = BinaryHeap()
        for row in row_t['test'][1:]:
            heap.add(User(*row.split(' ')))

        test(heapsort, idx, row_t['answer'], [heap])
