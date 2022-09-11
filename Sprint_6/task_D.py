import os
import sys
import time

sys.path.append(os.getcwd())
from tools import test

import collections
from itertools import groupby


def bfs(graph, start_point: int):
    if not graph:
        return [start_point]

    q = collections.deque([start_point])
    visited = set([start_point])

    response = []
    while q:
        v = q.popleft()
        response.append(v)
        print(str(v) + " ", end="")
        for w in graph[v]:
            if w not in visited:
                q.append(w)
                visited.add(w)
    
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
        k: [v[1] for v in g] for k, g in groupby(sorted(edges), lambda e: e[0])
    }

    for i in range(1, cnt_vertexes+1):
        if graph.get(i) is None:
            graph[i] = []

    bfs(graph, start_point)


tests = [
    {"test": [
        "4 4",
        "1 2",
        "2 3",
        "3 4",
        "1 4",
        "3",
    ], "answer": "3 2 4 1"},
    {"test": [
        "2 1",
        "2 1",
        "1",
    ], "answer": "1 2"},
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
            k: [v[1] for v in g] for k, g in groupby(sorted(edges), lambda e: e[0])
        }

        for i in range(1, cnt_vertexes+1):
            if graph.get(i) is None:
                graph[i] = []

        response = ' '.join(str(i) for i in bfs(graph, start_point))
        stop_t = time.time()

        test(None, idx, row['answer'], None, response, start_t, stop_t)
