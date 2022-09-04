# 69718799

"""
-- ПРИНЦИП РАБОТЫ --
    Идея удаления элемента делится на несколько случаев:
            1) у узла нет дочерних узлов;
            2) у узла есть левый дочерних узлов;
            3) у узла есть правый дочерних узлов;
            4) у узла есть оба ребёнка.
        В случае 1 просто удаляем узел, дополнительная работа не требуется.
        В случае 2 и 3 заменяем удаляемый узел на его потомка, на этом удаление заканчивается.
        В случае 4 находим в правом поддереве минимальный элемент и перемещаем его на место удаляемого узла.

    Идею удаления взял из этой статьи - https://tproger.ru/articles/dvoichnoe-binarnoe-derevo-udalenie-jelementa-i-skorost-raboty/

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    Наихудшая временная сложность операции удаления - O(h), где h - высота дерева.
    В худшем случае нам, возможно, придется путешествовать от корня к самому глубокому узлу.
    Высота перекошенного дерева может стать n, а временная сложность операции удаления - O(n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Этот алгоритм использует O(h) дополнительной памяти, где h - высота дерева. 
"""


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root

    def remove(self, value: int) -> Node:
        if not self.root:
            return self.root
        
        return self._delete_node(self.root, value)

    def _delete_node(self, node: Node, value: int) -> Node:
        if node.value == value:
            if node.right and node.left:
                min_node = self._find_min_elem(node.right)
                node.value = min_node.value

                node.right = self._delete_node(node.right, min_node.value)

            elif node.left:
                return node.left
            else:
                return node.right
        else:
            if node.value > value and node.left:
                node.left = self._delete_node(node.left, value)
            elif node.right:
                node.right = self._delete_node(node.right, value)
        
        return node

    def _find_min_elem(self, root: Node) -> Node:
        return self._find_min_elem(root.left) if root.left else root


def remove(root: Node, key: int):
    return BinaryTree(root).remove(key)
