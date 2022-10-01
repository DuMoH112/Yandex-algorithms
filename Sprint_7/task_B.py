import os
import sys

sys.path.append(os.getcwd())
from tools import test


def schedule(cnt_classes, sched):
    sched = sorted(sched, key=lambda v: [v[1], v[0]])
    result = [sched[0]]
    for lesson in sched[1:]:
        if lesson[0]>=result[-1][1]:
            result.append(lesson)
    
    print("\n".join(i for i in [str(len(result))] + [f'{s} {e}' for s,e in result]))
    return [str(len(result))] + [f'{s} {e}' for s,e in result]


def main():
    cnt_classes = int(input())
    sched = []
    for _ in range(cnt_classes):
        s, e = map(eval, input().split(' '))
        sched.append((s, e))
    schedule(cnt_classes, sched)


tests = [
    {"test": [
        "5",
        "9 10",
        "9.3 10.3",
        "10 11",
        "10.3 11.3",
        "11 12",
    ], "answer": [
        "3",
        "9 10",
        "10 11",
        "11 12",
    ]},
    {"test": [
        "3",
        "9 10",
        "11 12.25",
        "12.15 13.3",
    ], "answer": [
        "2",
        "9 10",
        "11 12.25",
    ]},
    {"test": [
        "7",
        "19 19",
        "7 14",
        "12 14",
        "8 22",
        "22 23",
        "5 21",
        "9 23",
    ], "answer": [
        "3",
        "7 14",
        "19 19",
        "22 23",
    ]},
    {"test": [
        "59",
        "15 22",
        "17 20",
        "12 13",
        "21 23",
        "15 15",
        "3 23",
        "20 23",
        "7 18",
        "11 13",
        "2 16",
        "7 19",
        "1 10",
        "16 23",
        "15 17",
        "15 19",
        "12 14",
        "8 9",
        "8 17",
        "19 23",
        "12 15",
        "3 10",
        "3 8",
        "17 20",
        "20 21",
        "0 0",
        "17 21",
        "13 17",
        "2 23",
        "20 20",
        "18 19",
        "9 10",
        "7 10",
        "23 23",
        "22 22",
        "8 10",
        "4 9",
        "21 21",
        "18 22",
        "14 19",
        "19 20",
        "22 23",
        "12 22",
        "3 9",
        "15 23",
        "2 21",
        "8 8",
        "10 15",
        "13 13",
        "0 7",
        "11 19",
        "0 22",
        "2 6",
        "15 16",
        "5 8",
        "20 23",
        "18 23",
        "11 22",
        "17 20",
        "12 14",
    ], "answer": [
        "17",
        "0 0",
        "2 6",
        "8 8",
        "8 9",
        "9 10",
        "11 13",
        "13 13",
        "15 15",
        "15 16",
        "18 19",
        "19 20",
        "20 20",
        "20 21",
        "21 21",
        "22 22",
        "22 23",
        "23 23",
    ]}
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        cnt_classes = int(row['test'][0])
        sched = []
        for string in row['test'][1:]:
            s, e = map(eval, string.split(' '))
            sched.append((s, e))

        test(schedule, idx, row['answer'], [cnt_classes, sched])
