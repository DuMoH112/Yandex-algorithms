import os
import sys
import time

sys.path.append(os.getcwd())
from tools import test


def create_adjacency_list(cnt_vertexes, graph):
    new_graph = [{
        'cnt_edges': 0,
        'vertexes': []
    } for i in range(cnt_vertexes)]

    for g in graph:
        from_ = g['from'] - 1
        to_ = g['to']
        new_graph[from_]['cnt_edges'] += 1
        new_graph[from_]['vertexes'].append(to_)

    return print_adjacency_list(new_graph)


def print_adjacency_list(graph):
    response = []
    for g in graph:
        if g['cnt_edges']:
            g['vertexes'].sort()
            vertexes = ' '.join(str(i) for i in g['vertexes'])
            response.append(f"{g['cnt_edges']} {vertexes}")
        else:
            response.append("0")

        print(response[-1])
    
    return response

tests = [
    {"test": [
        "5 3",
        "1 3",
        "2 3",
        "5 2",
    ], "answer": [
        "1 3",
        "1 3",
        "0",
        "0",
        "1 2",
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

        test(create_adjacency_list, idx, row['answer'], [cnt_vertexes, graph])
