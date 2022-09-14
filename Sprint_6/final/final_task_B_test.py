import os
import sys

from final_task_B import railroad, RoadsType, UnknownRoadException

sys.path.append(os.getcwd())
from tools import test

praktikum_tests = [
    {"test": [
        "3",
        "RB",
        "R",
    ], "answer": "NO"},
    {"test": [
        "4",
        "BBB",
        "RB",
        "B",
    ], "answer": "YES"},
    {"test": [
        "5",
        "RRRB",
        "BRR",
        "BR",
        "R",
    ], "answer": "NO"},
    {"test": [
        "10",
        "RRBRRBRRR",
        "BBBBBBRB",
        "BBRBRRR",
        "RRBRRR",
        "RBRRR",
        "BBRR",
        "RRR",
        "RR",
        "B",
    ], "answer": "YES"}
]


if __name__ == '__main__':
    for idx, row_t in enumerate(praktikum_tests):
        cnt_cities = int(row_t['test'][0])

        graph = {v: [] for v in range(cnt_cities)}

        for i, row in enumerate(row_t['test'][1:]):
            for j, type_road in enumerate(row.rstrip()):
                if type_road == RoadsType.HIGHWAY:
                    graph[i].append(i+j+1)
                elif type_road == RoadsType.ROAD:
                    graph[i+j+1].append(i)
                else:
                    raise UnknownRoadException

        response = railroad(cnt_cities, graph)
        print("NO" if response else "YES")
        test(None, idx, row_t['answer'], None, "NO" if response else "YES")
