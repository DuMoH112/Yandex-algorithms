from final_task_B import remove, Node


def tests():
    test1()
    test2()


def test1():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    root = Node(node3, node6, 5)
    newHead = remove(root, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8
    print("Test 1 is \033[92mOK\033[0m")
    #             5
    #       1           10
    #    -    3        8   -
    #       2   -    6   -


def test2():
    node10 = Node(None, None, 99)
    node9 = Node(None, None, 72)
    node8 = Node(node9, node10, 91)
    node7 = Node(None, None, 50)
    node6 = Node(None, None, 32)
    node5 = Node(None, node6, 29)
    node4 = Node(None, None, 11)
    node3 = Node(node7, node8, 65)
    node2 = Node(node4, node5, 20)
    root = Node(node2, node3, 41)
    newHead = remove(root, 41)
    assert newHead.value == 50
    assert newHead.right is node3
    assert newHead.right.value == 65
    print("Test 2 is \033[92mOK\033[0m")
    #             41
    #       20           65
    #    11    29      50   91
    #         -  32       72  99


tests()

    