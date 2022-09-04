import os
import sys

from final_task_B import main, Person

sys.path.append(os.getcwd())
from tools import test

tests = [
    {
        "test": [
            "5",
            "gena 0 0",
            "alla 0 0",
            "rita 0 0",
            "gosha 0 0",
            "timofey 0 0",
        ],
        "answer": [
            "alla",
            "gena",
            "gosha",
            "rita",
            "timofey",
        ]
    },
    {
        "test": [
            "5",
            "alla 0 0",
            "gena 0 0",
            "gosha 0 0",
            "rita 0 0",
            "timofey 0 0",
        ],
        "answer": [
            "alla",
            "gena",
            "gosha",
            "rita",
            "timofey",
        ]
    },
    {
        "test": [
            "5",
            "alla 4 100",
            "gena 6 1000",
            "gosha 2 90",
            "rita 2 90",
            "timofey 4 80",
        ],
        "answer": [
            "gena",
            "timofey",
            "alla",
            "gosha",
            "rita",
        ]
    },
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        cnt_students = int(row['test'][0])
        students = [Person(*string.split(' ')) for string in row['test'][1:]]

        test(main, idx, tests[idx]['answer'], [cnt_students, students])
