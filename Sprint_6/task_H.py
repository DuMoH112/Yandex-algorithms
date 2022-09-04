import os
import sys
import time

import networkx as nx
import matplotlib.pyplot as plt

sys.path.append(os.getcwd())
from tools import test

from itertools import groupby


def dfs(graph, start_point: int):
    if not graph:
        return [start_point]

    stack = [start_point]
    response = {}
    time = 0
    while stack:
        v = graph[stack.pop()]
        if v['color'] == 'white':
            v['color'] = 'gray'
            stack.append(v['key'])
            response[v['key']] = {
                'start': time,
                'stop': None
            }

            for edge in v['edges'][::-1]:
                w = graph[edge]
                if w['color'] == 'white':
                    stack.append(w['key'])
        elif v['color'] == 'gray':
            v['color'] = 'black'
            response[v['key']]['stop'] = time
            print(response[v['key']]['start'], response[v['key']]['stop'])
        
        time += 1
    
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


def visualedGraph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True, arrowstyle='-|>')    
    plt.show()


if __name__ == '__main__':
    for idx, row in enumerate(tests):
        start_t = time.time()
        cnt_vertexes, cnt_edges = map(int, row['test'][0].split(' '))

        edges = []
        for row_ in row['test'][1:-1]:
            from_, to_ = map(int, row_.split())
            edges.append([to_, from_])

        graph = {
            k: {
                'key': k,
                'edges': [v[1] for v in g],
                'color': 'white'
            } for k, g in groupby(sorted(edges), lambda e: e[0])
        }

        for i in range(1, cnt_vertexes+1):
            if graph.get(i) is None:
                graph[i] = {
                    'key': i,
                    'edges': [],
                    'color': 'white'
                }

        response = dfs(graph, 1)
        [print(response[i]) for i in response]
        stop_t = time.time()

        test(None, idx, row['answer'], None, response, start_t, stop_t)
