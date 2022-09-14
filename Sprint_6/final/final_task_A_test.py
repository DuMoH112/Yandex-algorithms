import os
import sys

from final_task_A import expensive_network, Graph

sys.path.append(os.getcwd())
from tools import test

praktikum_tests = [
    {"test": [
        "4 4",
        "1 2 5",
        "1 3 6",
        "2 4 8",
        "3 4 3",
    ], "answer": 19},
    {"test": [
        "3 3",
        "1 2 1",
        "1 2 2",
        "2 3 1",
    ], "answer": 3},
    {"test": [
        "2 0",
    ], "answer": "Oops! I did it again"},
    {"test": [
        "1 0",
    ], "answer": 0},
    {"test": [
        "12 17",
        "1 2 5",
        "1 12 1",
        "12 11 9",
        "2 11 7",
        "2 3 8",
        "11 4 6",
        "3 4 3",
        "3 5 13",
        "4 10 6",
        "4 5 2",
        "5 10 10",
        "5 6 12",
        "6 7 13",
        "7 10 8",
        "7 8 16",
        "8 9 1",
        "9 10 5",
    ], "answer": 104},
]


if __name__ == '__main__':
    for idx, row_t in enumerate(praktikum_tests):
        cnt_vertexes, cnt_edges = map(int, row_t['test'][0].split(' '))

        graph = Graph(cnt_vertexes)
        for row in row_t['test'][1:]:
            graph.add_edge(*map(int, row.split()))

        test(expensive_network, idx, row_t['answer'], [graph])
