# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def isBST(node: Node, isStart: bool = True):
    if not node:
        return True, None, None

    is_bst_l, min_l, max_l = isBST(node.left, False)
    is_bst_r, min_r, max_r = isBST(node.right, False)

    is_bst = is_bst_l and is_bst_r and \
        (max_l is None or node.value > max_l) and \
        (min_r is None or node.value < min_r)

    min_value = min([i for i in [min_l, node.value, min_r] if i])
    max_value = max([i for i in [max_l, node.value, max_r] if i])

    if isStart:
        return is_bst

    return is_bst, min_value, max_value


def solution(root: Node) -> bool:
    return isBST(root)


# def test():
#     node1 = Node(1, None, None)
#     node2 = Node(4, None, None)
#     node3 = Node(3, node1, node2)
#     node4 = Node(8, None, None)
#     node5 = Node(5, node3, node4)

#     assert solution(node5)
#     node2.value = 5
#     assert not solution(node5)


# test()
