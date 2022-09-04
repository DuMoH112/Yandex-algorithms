import os
import sys
import time

sys.path.append(os.getcwd())
from tools import test

from bisect import insort


def dfs(cnt_vertexes, graph, start_point: int):
    stack = [start_point]

    time = 0
    color = ['white'] * (cnt_vertexes + 1)
    entry = [None] * (cnt_vertexes + 1)
    leave = [None] * (cnt_vertexes + 1)

    while stack:
        v = stack.pop()
        if color[v] == 'black':
            continue

        if color[v] == 'white':
            color[v] = 'gray'
            stack.append(v)
            entry[v] = time

            for w in graph[v][::-1]:
                if color[w] == 'white':
                    stack.append(w)
        elif color[v] == 'gray':
            color[v] = 'black'
            leave[v] = time
            
        time += 1
    
    return entry, leave


def main():
    cnt_vertexes, cnt_edges = map(int, input().split(' '))

    edges = []
    for _ in range(cnt_edges):
        from_, to_ = map(int, input().split())
        edges.append([from_, to_])

    graph = {}
    for start, end in edges:
        if not graph.get(start):
            graph[start] = [end]
        else:
            insort(graph[start], end)

    for i in range(1, cnt_vertexes+1):
        if graph.get(i) is None:
            graph[i] = []

    entry, leave = dfs(cnt_vertexes, graph, 1)
    for i in range(1, cnt_vertexes+1):
        print(f"{entry[i]} {leave[i]}")


tests = [
    {"test": [
        "6 8",
        "2 6",
        "1 6",
        "3 1",
        "2 5",
        "4 3",
        "3 2",
        "1 2",
        "1 4",
    ], "answer": [
        "0 11",
        "1 6",
        "8 9",
        "7 10",
        "2 3",
        "4 5",
    ]},
    {"test": [
        "3 2",
        "1 2",
        "2 3",
    ], "answer": [
        "0 5",
        "1 4",
        "2 3",
    ]},
]


if __name__ == '__main__':
    for idx, row in enumerate(tests):
        start_t = time.time()
        cnt_vertexes, cnt_edges = map(int, row['test'][0].split(' '))

        edges = []
        for row_ in row['test'][1:]:
            from_, to_ = map(int, row_.split())
            edges.append([from_, to_])

        graph = {}
        for start, end in edges:
            if not graph.get(start):
                graph[start] = [end]
            else:
                insort(graph[start], end)

        for i in range(1, cnt_vertexes+1):
            if graph.get(i) is None:
                graph[i] = []

        entry, leave = dfs(cnt_vertexes, graph, 1)
        response = []
        for i in range(1, cnt_vertexes+1):
            response.append(f"{entry[i]} {leave[i]}")

        [print(i) for i in response]
        stop_t = time.time()

        test(None, idx, row['answer'], None, response, start_t, stop_t)
