import sys
from time import time


def test_func(func):
    tests = {
        "task_A": [
            {"test": [
                "4",
                "3",
                "1 2 3",
                "0 2 6",
                "7 4 1",
                "2 7 0"
            ], "answer": [
                "1 0 7 2",
                "2 2 4 7",
                "3 6 1 0"
            ]},
            {"test": [
                "9",
                "5",
                "-7 -1 0 -4 -9",
                "5 -1 2 2 9",
                "3 1 -8 -1 -7",
                "9 0 8 -8 -1",
                "2 4 5 2 8",
                "-7 10 0 -4 -8",
                "-3 10 -7 10 3",
                "1 6 -7 -5 9",
                "-1 9 9 1 9"
            ], "answer": [
                "-7 5 3 9 2 -7 -3 1 -1",
                "-1 -1 1 0 4 10 10 6 9",
                "0 2 -8 8 5 0 -7 -7 9",
                "-4 2 -1 -8 2 -4 10 -5 1",
                "-9 9 -7 -1 8 -8 3 9 9"
            ]}
        ],
        "task_F": [
            {"test": [
                "8",
                "get_max",
                "push 7",
                "pop",
                "push -2",
                "push -1",
                "pop",
                "get_max",
                "get_max"
            ], "answer": [
                "None",
                "-2",
                "-2"
            ]},
            {"test": [
                "7",
                "get_max",
                "pop",
                "pop",
                "pop",
                "push 10",
                "get_max",
                "push -9"
            ], "answer": [
                "None",
                "error",
                "error",
                "error",
                "10"
            ]}
        ],
        "task_G": [
            {"test": [
                "10",
                "pop",
                "pop",
                "push 4",
                "push -5",
                "push 7",
                "pop",
                "pop",
                "get_max",
                "pop",
                "get_max"
            ], "answer": [
                "error",
                "error",
                "4",
                "None"
            ]},
            {"test": [
                "10",
                "get_max",
                "push -6",
                "pop",
                "pop",
                "get_max",
                "push 2",
                "get_max",
                "pop",
                "push -2",
                "push -6"
            ], "answer": [
                "None",
                "error",
                "None",
                "2"
            ]},
            {"test": [
                "31",
                "get_max",
                "push -7",
                "pop",
                "get_max",
                "pop",
                "push 2",
                "get_max",
                "pop",
                "get_max",
                "push 7",
                "push -5",
                "pop",
                "push -6",
                "pop",
                "get_max",
                "pop",
                "get_max",
                "get_max",
                "pop",
                "push -4",
                "push 10",
                "push -8",
                "push -6",
                "push -10",
                "push 0",
                "pop",
                "push 7",
                "get_max",
                "push 3",
                "push -10",
                "get_max"
            ], "answer": [
                "None",
                "None",
                "error",
                "2",
                "None",
                "7",
                "None",
                "None",
                "error",
                "10",
                "10"
            ]}
        ],
        "task_H": [
            {"test": "{[()]}", "answer": True},
            {"test": "{[]}()", "answer": True},
            {"test": "{[()]", "answer": False},
            {"test": "()", "answer": True},
            {"test": "{[)]}", "answer": False},
            {"test": "{", "answer": False}
        ],
        "task_I": [
            {"test": [
                "8",
                "2",
                "peek",
                "push 5",
                "push 2",
                "peek",
                "size",
                "size",
                "push 1",
                "size",
            ], "answer": [
                "None",
                "5",
                "2",
                "2",
                "error",
                "2",
            ]},
            {"test": [
                "10",
                "1",
                "push 1",
                "size",
                "push 3",
                "size",
                "push 1",
                "pop",
                "push 1",
                "pop",
                "push 3",
                "push 3",
            ], "answer": [
                "1",
                "error",
                "1",
                "error",
                "1",
                "1",
                "error",
            ]}
        ],
        "task_J": [
            {"test": [
                "10",
                "put -34",
                "put -23",
                "get",
                "size",
                "get",
                "size",
                "get",
                "get",
                "put 80",
                "size",
            ], "answer": [
                "-34",
                "1",
                "-23",
                "0",
                "error",
                "error",
                "1",
            ]},
            {"test": [
                "6",
                "put -66",
                "put 98",
                "size",
                "size",
                "get",
                "get",
            ], "answer": [
                "2",
                "2",
                "-66",
                "98",
            ]},
            {"test": [
                "9",
                "get",
                "size",
                "put 74",
                "get",
                "size",
                "put 90",
                "size",
                "size",
                "size",
            ], "answer": [
                "error",
                "0",
                "74",
                "0",
                "1",
                "1",
                "1",
            ]},
            {"test": [
                "8",
                "get",
                "size",
                "size",
                "size",
                "put 50",
                "put 60",
                "put 89",
                "put 72",
            ], "answer": [
                "error",
                "0",
                "0",
                "0",
            ]}
        ],
        "task_K": [
            {"test": "3", "answer": "3"},
            {"test": "0", "answer": "1"},
        ],
        "task_L": [
            {"test": "3 1", "answer": "3"},
            {"test": "10 1", "answer": "9"},
        ],
    }

    for index, row in enumerate(tests[func.__name__]):
        start_t = time()
        response, byte_size = func(row['test'])
        end_t = time()
        print(f"""     
Test {index + 1} is {response == row['answer']}
Time done: {"{:.7f}".format(end_t - start_t)}
Memory size (MByte): {byte_size/1024}
""")

    return


def task_A(test = None):
    cnt_rows, cnt_cols, matrix = None, None, None
    byte_size = 0
    if test:
        cnt_rows = int(test[0])
        cnt_cols = int(test[1])
        matrix = [[str(col) for col in str(test[i_row + 2]).split(" ")]
                  for i_row in range(cnt_rows)]
    else:
        cnt_rows = int(input())
        cnt_cols = int(input())
        matrix = [[str(col) for col in input().split(" ")]
                  for i_row in range(cnt_rows)]

    byte_size += sys.getsizeof(matrix) + \
        sys.getsizeof(cnt_cols) + \
        sys.getsizeof(cnt_rows)

    return [" ".join([matrix[j][i] for j in range(cnt_rows)]) for i in range(cnt_cols)], byte_size


def task_F(test=None):
    cnt_command, commands = None, None
    if test:
        cnt_command = int(test[0])
        commands = [test[i + 1].split(' ') for i in range(cnt_command)]
    else:
        cnt_command = int(input())
        commands = [input().split(' ') for i in range(cnt_command)]

    class Stack:
        def __init__(self):
            self.items = []
            self.length = 0

        def push(self, item):
            self.length += 1
            self.items.append(item)

        def pop(self):
            if self.length:
                self.length -= 1
                self.items.pop()
            else:
                print("error")
                return "error"

        def get_max(self):
            max_item = max(self.items) if self.length else None
            print(max_item)
            return str(max_item)

    def main(commands):
        s = Stack()
        res = []
        for com in commands:
            func, item = com[0], None
            if len(com) > 1:
                item = int(com[1])

            if func == "push":
                s.push(item)
            elif func == "get_max":
                res.append(s.get_max())
            elif func == "pop":
                r = s.pop()
                if r:
                    res.append(r)

        return res

    res = main(commands)
    return res, 0


def task_G(test=None):
    cnt_command, commands = None, None
    if test:
        cnt_command = int(test[0])
        commands = [test[i + 1].split(' ') for i in range(cnt_command)]
    else:
        cnt_command = int(input())
        commands = [input().split(' ') for i in range(cnt_command)]

    class Stack:
        def __init__(self):
            self.items = []
            self.length = 0
            self.max_list = []

        def push(self, item):
            self.length += 1
            self.items.append(item)

            self.max_list.append(
                item
                if self.length == 1 or item > self.max_list[-1]
                else self.max_list[-1])

        def pop(self):
            if self.length:
                self.length -= 1
                self.items.pop()
                self.max_list.pop()
            else:
                print("error")
                return "error"

        def get_max(self):
            max_item = self.max_list[-1] if self.length else None
            print(max_item)
            return str(max_item)

    def main(commands):
        s = Stack()
        for com in commands:
            func, *item = com
            if item:
                item = int(item[0])

            if func == "push":
                s.push(item)
            elif func == "get_max":
                s.get_max()
            elif func == "pop":
                s.pop()

        return []

    res = main(commands)
    return res, 0


def task_H(test: str = None):
    string = None
    byte_size = 0
    if test:
        string = test
    else:
        string = input()

    def isBracketSequence(string):
        open_brackets = ["[", "{", "("]
        close_brackets = ["]", "}", ")"]
        stack = []
        len_stack = 0

        for char in string:
            if char in open_brackets:
                stack.append(char)
                len_stack += 1
            elif char in close_brackets:
                pos = close_brackets.index(char)
                if (len_stack > 0 and open_brackets[pos] == stack[-1]):
                    stack.pop()
                    len_stack -= 1
                else:
                    return False
        if len_stack > 0:
            return False

        return True

    res = isBracketSequence(string)
    return res, byte_size


def task_I(test=None):
    cnt_command, commands = None, None
    if test:
        cnt_command = int(test[0])
        len_queue = int(test[1])
        commands = [test[i + 2].split(' ') for i in range(cnt_command)]
    else:
        cnt_command = int(input())
        len_queue = int(input())
        commands = [input().split(' ') for i in range(cnt_command)]

    class Queue:
        def __init__(self, n):
            self.queue = [None] * n
            self.max_n = n
            self.head = 0
            self.tail = 0
            self.size = 0

        def push(self, item):
            if self.size != self.max_n:
                self.queue[self.tail] = item
                self.tail = (self.tail + 1) % self.max_n
                self.size += 1
                return ""
            else:
                print("error")
                return "error"

        def peek(self):
            if self.size == 0:
                print(None)
                return None
            print(self.queue[self.head])
            return self.queue[self.head]

        def pop(self):
            if self.size == 0:
                print(None)
                return None

            item = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            print(item)
            return item

    def main(commands, len_queue):
        q = Queue(len_queue)
        res = []
        for com in commands:
            func, *item = com
            if item:
                item = int(item[0])

            r = ""
            if func == "push":
                r = q.push(item)
            elif func == "peek":
                r = q.peek()
            elif func == "pop":
                r = q.pop()
            elif func == "size":
                r = q.size

            if r in [None, "error"] or r != "":
                res.append(str(r))

        print()
        [print(i) for i in res]
        return res
    res = main(commands, len_queue)
    return res, 0


def task_J(test=None):
    cnt_command, commands = None, None
    if test:
        cnt_command = int(test[0])
        commands = [test[i + 1].split(' ') for i in range(cnt_command)]
    else:
        cnt_command = int(input())
        commands = [input().split(' ') for i in range(cnt_command)]

    class Node:
        def __init__(self, value=None, next_item=None):
            self.value = value
            self.next = next_item

        def __str__(self):
            return str(self.value)

    class Queue:
        def __init__(self):
            self.size = 0
            self.head = Node()
            self.tail = Node()

        def __str__(self):
            return str(self.value)

        def put(self, item):
            if self.size == 0:
                self.head = Node(item)
                self.tail = self.head
            else:
                self.tail.next = Node(item)
                self.tail.next.next = self.head
                self.tail = self.tail.next

            self.size += 1

        def get(self):
            item = None
            if self.size == 0:
                # print('error')
                return 'error'
            elif self.size == 1:
                item = self.head
                self.head = Node()
                self.tail = Node()
            elif self.size == 2:
                item = self.head
                self.head = self.tail
            else:
                item = self.head
                self.head = self.tail.next.next
                self.tail.next = self.head

            self.size -= 1
            # print(item)
            return item

    def main(commands):
        q = Queue()
        res = []
        for com in commands:
            func, *item = com
            if item:
                item = int(item[0])

            r = None
            if func == "put":
                r = q.put(item)
            elif func == "get":
                r = q.get()
            elif func == "size":
                # print(q.size)
                r = q.size

            if r == "error" or r != None:
                res.append(str(r))

        print()
        [print(i) for i in res]
        return res
    res = main(commands)
    return res, 0


def task_K(test: str = None):
    n = None
    byte_size = 0
    if test:
        n = int(test)
    else:
        n = int(input())

    def fibonachi(n):
        if n == 0 or n == 1:
            return 1
        else:
            return fibonachi(n - 1) + fibonachi(n - 2)

    res = fibonachi(n)
    print("res", res)
    return str(res), byte_size


def task_L(test: str = None):
    n = None
    byte_size = 0
    if test:
        n, k = [int(i) for i in test.split(' ')]
    else:
        n, k = [int(i) for i in input().split(' ')]

    d = 10 ** k
    result = 1
    n_1 = 1
    n_2 = 1
    if n >= 2:
        n -= 1
        for i in range(n):
            s = (n_1 + n_2) % d
            n_1, n_2 = n_2, s
            result = n_2
    print("res", result)
    return str(result), byte_size


test_func(task_L)
