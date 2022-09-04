import os
import sys
import time

sys.path.append(os.getcwd())
from tools import test

from itertools import groupby


def dfs(graph, start_point: int):
    if not graph:
        return [start_point]

    visited = set()
    stack = [start_point]
    response = []
    while stack:
        v = graph[stack.pop()]
        if v['key'] not in visited:
            visited.add(v['key'])
            stack.append(v['key'])
            response.append(v['key'])
            for edge in v['edges'][::-1]:
                w = graph[edge]
                if w['key'] not in visited:
                    stack.append(w['key'])
    
    return response


def main():
    cnt_vertexes, cnt_edges = map(int, input().split(' '))

    edges = []
    for _ in range(cnt_edges):
        from_, to_ = map(int, input().split())
        edges.append([to_, from_])
        edges.append([from_, to_])

    start_point = int(input())

    graph = {
        k: {
            'key': k,
            'edges': [v[1] for v in g]
        } for k, g in groupby(sorted(edges), lambda e: e[0])
    }

    for i in range(1, cnt_vertexes+1):
        if graph.get(i) is None:
            graph[i] = {
                'key': i,
                'edges': []
            }

    print(*dfs(graph, start_point))


tests = [
    {"test": [
        "4 4",
        "3 2",
        "4 3",
        "1 4",
        "1 2",
        "3",
    ], "answer": "3 2 1 4"},
    {"test": [
        "2 1",
        "1 2",
        "1",
    ], "answer": "1 2"},
    {"test": [
        "3 1",
        "2 3",
        "1",
    ], "answer": "1"},
    {"test": [
        "6 7",
        "3 2",
        "5 4",
        "3 1",
        "1 4",
        "1 6",
        "1 2",
        "1 5",
        "1",
    ], "answer": "1 2 3 4 5 6"},
    {"test": [
        "1 0",
        "1",
    ], "answer": "1"},
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        start_t = time.time()
        cnt_vertexes, cnt_edges = map(int, row['test'][0].split(' '))

        edges = []
        for row_ in row['test'][1:-1]:
            from_, to_ = map(int, row_.split())
            edges.append([to_, from_])
            edges.append([from_, to_])

        start_point = int(row['test'][-1])

        graph = {
            k: {
                'key': k,
                'edges': [v[1] for v in g]
            } for k, g in groupby(sorted(edges), lambda e: e[0])
        }

        for i in range(1, cnt_vertexes+1):
            if graph.get(i) is None:
                graph[i] = {
                    'key': i,
                    'edges': []
                }

        response = ' '.join(str(i) for i in dfs(graph, start_point))
        stop_t = time.time()

        test(None, idx, row['answer'], None, response, start_t, stop_t)
