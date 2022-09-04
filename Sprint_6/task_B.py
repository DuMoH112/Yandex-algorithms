from tools import test
import os
import sys
import time

sys.path.append(os.getcwd())


def create_adjacency_matrix(cnt_vertexes, graph):
    new_graph = [[0 for i in range(cnt_vertexes)] for i in range(cnt_vertexes)]

    for g in graph:
        from_ = g['from'] - 1
        to_ = g['to'] - 1
        new_graph[from_][to_] = 1

    return print_adjacency_matrix(new_graph)


def print_adjacency_matrix(graph):
    response = []
    for g in graph:
        row = ' '.join(str(i) for i in g)
        response.append(row)
        print(row)

    return response


def start():
    r1 = input().split(' ')
    cnt_vertexes, cnt_edges = int(r1[0]), int(r1[1])
    graph = []
    for row_ in range(cnt_edges):
        from_, to_ = input().split(' ')
        graph.append({
            'from': int(from_),
            'to': int(to_)
        })

    create_adjacency_matrix(cnt_vertexes, graph)


tests = [
    {"test": [
        "5 3",
        "1 3",
        "2 3",
        "5 2",
    ], "answer": [
        "0 0 1 0 0",
        "0 0 1 0 0",
        "0 0 0 0 0",
        "0 0 0 0 0",
        "0 1 0 0 0",
    ]}
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        r1 = row['test'][0].split(' ')
        cnt_vertexes, cnt_edges = int(r1[0]), int(r1[1])
        graph = []
        for row_ in row['test'][1:]:
            from_, to_ = row_.split(' ')
            graph.append({
                'from': int(from_),
                'to': int(to_)
            })

        test(create_adjacency_matrix, idx,
             row['answer'], [cnt_vertexes, graph])
