# 70329555

"""
-- ПРИНЦИП РАБОТЫ --
    1. Из входных данных составляем неориентированный взвешенный граф.
       При формировании графа веса сохраняются с отрицательным префиксом, что позволит дальше
       в куче хранить максимальное значение в начале списка

    2. Составление максимального остового дерева происходит при помощи Алгоритм Прима с использованием кучи.
       Для формирования кучи используется библиотека - heapq

    2.1. Функция add_vertex служит для добавления вершины в остов, с проверкой исходящех рёбер данной вершины
         на отсутствие данных вершин ребра во множестве вершин добавленных в остов.
    
    2.2. Функция expensive_network - это функция поиска максимального остового дерева. На вход подаётся граф
         и начиная с первой вершины начиается обход. Далее пробегаемся циклом, пока длина множества added
         не равна значению вершин в графе и массив (куча) существуют (имеет элементы),
         берем "минимальный" (максимальный) элемент из кучи edges. Проверяем, что вершины этого ребра
         нет во множестве вершин, добавленных в остов и, в таком случае, к значению максимального остовного дерева
         max_spanning_tree прибавляем вес максимального ребра, как раз того, что мы
         забарали из кучи. После чего вызваем функцию add_vertex() для добавления данной вершины в остов.
         Когда цикл завершится, необходимо проверить, что длина множества added равно количеству вершин графа.
         В этом случае вернем значение max_spanning_tree, что и будет передавать значение максимального остовного дерева.
        
         В противном случае, если в графе несколько компонент связности, выведем сообщение: 'Oops! I did it again'.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    O(E*logV), где E - количество рёбер в графе, а V - количество вершин.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(n)   - Хранение кучи.
    O(E*V) - Список смежности где E - количество вершин, V - количество рёбер.
"""


from typing import List, Dict, Tuple
import heapq

type_edges = List[Tuple[int, int]]


class Graph:
    def __init__(self, cnt_vertexes: int):
        self.graph: Dict[int, type_edges] = {
            i: [] for i in range(1, cnt_vertexes+1)
        }
        self.size: int = cnt_vertexes

    def __getitem__(self, vertex: int) -> type_edges:
        return self.graph.get(vertex, [])

    def add_edge(self, start: int, end: int, weight: int):
        self.graph[start].append((-weight, end))
        self.graph[end].append((-weight, start))


def add_vertex(vertex: int, graph_edges: type_edges, added: List[bool], edges: List[type_edges]):
    added[vertex] = True

    for weight, end in graph_edges:
        if not added[end]:
            heapq.heappush(edges, (weight, end))


def expensive_network(graph: Graph):
    max_spanning_tree = 0
    added = [False] * (graph.size + 1)
    edges = []

    added[0] = True
    add_vertex(1, graph[1], added, edges)
    while not all(added) and edges:
        weight, end = heapq.heappop(edges)
        if not added[end]:
            max_spanning_tree += abs(weight)
            add_vertex(end, graph[end], added, edges)

    return 'Oops! I did it again' if not all(added) else max_spanning_tree


if __name__ == '__main__':
    cnt_vertexes, cnt_edges = map(int, input().split(' '))

    graph = Graph(cnt_vertexes)
    for _ in range(cnt_edges):
        graph.add_edge(*map(int, input().split()))

    print(expensive_network(graph))
