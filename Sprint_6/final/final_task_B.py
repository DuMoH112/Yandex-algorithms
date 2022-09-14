# 70437407

"""
-- ПРИНЦИП РАБОТЫ --
    1. Из входных данных составляем ориентированный граф с учётом условия,
       где между вершинами существует разные типы дорог:
            HIGHWAY = 'B'
            ROAD = 'R'
    
    2. Для каждой вершины запускаем обход DFS, если граф имеет цикл, значит путь неоптимальный.
       За обход отвечает функция is_cyclic. 
    
    2.1. Формируется список цветов для каждой вершины, где:
            WHITE - вершина не посещена
            GRAY - вершина посещена, но не до конца обработана
            BLACK - вершина посещена и обработана
    
    Таким образом, если в процессе обхода графа мы наткнемся на серую вершину, то это означает, что в графе есть цикл.
    Это означает, что существует пара вершин, между которыми есть маршрут с разным типом дорог и
    карта железных дорог в этом случае является не оптимальной.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(V+E) - DFS.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(E*V) - Список смежности где E - количество вершин, V - количество рёбер.
"""

from typing import List


class UnknownRoadException(Exception):
    def __init__(self):
        pass


class RoadsType:
    HIGHWAY = 'B'
    ROAD = 'R'


class Color:
    WHITE = 0
    GRAY = 1
    BLACK = 2


def is_cyclic(graph, start_point: int, colors: List[Color]):
    stack = [start_point]

    while stack:
        v = stack.pop()
        if colors[v] == Color.WHITE:
            colors[v] = Color.GRAY
            stack.append(v)

            for w in graph[v]:
                if colors[w] == Color.WHITE:
                    stack.append(w)
                elif colors[w] == Color.GRAY:
                    return True
        elif colors[v] == Color.GRAY:
            colors[v] = Color.BLACK

    return False


def railroad(cnt_cities: int, graph):
    colors = [Color.WHITE for _ in range(cnt_cities)]
    for start_point in range(cnt_cities):
        if is_cyclic(graph, start_point, colors):
            return True
    return False


if __name__ == '__main__':
    cnt_cities = int(input())

    graph = {v: [] for v in range(cnt_cities)}

    for i in range(cnt_cities-1):
        for j, type_road in enumerate(input().rstrip()):
            if type_road == RoadsType.HIGHWAY:
                graph[i].append(i+j+1)
            elif type_road == RoadsType.ROAD:
                graph[i+j+1].append(i)
            else:
                raise UnknownRoadException

    print("NO" if railroad(cnt_cities, graph) else "YES")
