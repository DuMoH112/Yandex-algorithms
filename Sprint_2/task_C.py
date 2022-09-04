# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1

    return node


def solution(head_node, idx):
    if idx == 0:
        return head_node.next_item
    previous_node = get_node_by_index(head_node, idx-1)
    del_node = previous_node.next_item
    previous_node.next_item = previous_node.next_item.next_item

    return head_node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    print_list(new_head)
    # result is node0 -> node2 -> node3


def print_list(node):
    while node.next_item:
        print(node.value, end=" -> ")
        node = node.next_item
    print(node.value, end=" -> ")


test()
