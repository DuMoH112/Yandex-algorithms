# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def find_max(val, max_val):
    return val if val > max_val else max_val


def dfs(root, max_value):
    max_value = find_max(root.value, max_value)

    if root.left:
        l_max = dfs(root.left, max_value)
        max_value = find_max(l_max, max_value)
    if root.right:
        r_max = dfs(root.right, max_value)
        max_value = find_max(r_max, max_value)

    return max_value


def solution(root: Node) -> int:
    return dfs(root, root.value)


# def test():
#     node1 = Node(1)
#     node2 = Node(-5)
#     node3 = Node(3, node1, node2)
#     node4 = Node(2, node3, None)
#     assert solution(node4) == 3


# test()
