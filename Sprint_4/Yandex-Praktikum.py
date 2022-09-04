import os
import sys
from time import time

sys.path.append(os.getcwd())
from tools import test, bcolors


def test_func(func):
    tests = {
        "task_A": [
            {"test": [
                "123",
                "100003",
                "a",
            ], "answer": "97"},
            {"test": [
                "123",
                "100003",
                "hash",
            ], "answer": "6080"},
            {"test": [
                "123",
                "100003",
                "HaSH",
            ], "answer": "56156"},
        ],
        "task_B": [
            {"test": "", "answer": "True"}
        ],
        "task_C": [
            {"test": [
                "1000",
                "1000009",
                "abcdefgh",
                "7",
                "1 1",
                "1 5",
                "2 3",
                "3 4",
                "4 4",
                "1 8",
                "5 8",
            ], "answer": [
                "97",
                "225076",
                "98099",
                "99100",
                "100",
                "436420",
                "193195",
            ]},
            {"test": [
                "100",
                "10",
                "a",
                "1",
                "1 1",
            ], "answer": ["7"]},
        ],
        "task_D": [
            {"test": [
                "8",
                "вышивание крестиком",
                "рисование мелками на парте",
                "настольный керлинг",
                "настольный керлинг",
                "кухня африканского племени ужасмай",
                "тяжелая атлетика",
                "таракановедение",
                "таракановедение",
            ], "answer": [
                "вышивание крестиком",
                "рисование мелками на парте",
                "настольный керлинг",
                "кухня африканского племени ужасмай",
                "тяжелая атлетика",
                "таракановедение",
            ]}
        ],
        "task_E": [
            # {"test": "abcabcbb", "answer": "3"},
            # {"test": "bbbbb", "answer": "1"},
            # {"test": "azx", "answer": "3"},
            # {"test": "ojodx", "answer": "4"},
            # {"test": "ysmfzgw", "answer": "7"},
            {"test": "mtwpyqlnlo", "answer": "8"},
            {"test": "lu", "answer": "2"},
        ]
    }

    for idx, row in enumerate(tests[func.__name__]):
        start_t = time()
        response = func(row['test'])
        end_t = time()

        test(None, idx, row['answer'], None, response, start_t, end_t)

    return


def task_A(test=None):
    a, s, m = None, None, None
    if test:
        a = int(test[0])
        m = int(test[1])
        s = test[2]
    else:
        a = int(input())
        m = int(input())
        s = input()

    def _hash(a, m, s):
        sum_hash = 0
        pow_a_n = 1
        for i, char in enumerate(s):
            sum_hash = (sum_hash + ord(char) * pow_a_n) % m
            pow_a_n = (pow_a_n * a) % m

        return sum_hash

    return str(_hash(a, m, s[::-1]))


def task_B(test=None):
    import random
    import string
    letters = list(string.ascii_lowercase)
    def generate_string(len_s):
        return "".join(random.choice(letters) for _ in range(len_s))

    def _hash(s, a=1000, m=123_987_123):
        sum_hash = 0
        pow_a_n = 1
        for i, char in enumerate(s):
            sum_hash = (sum_hash + ord(char) * pow_a_n) % m
            pow_a_n = (pow_a_n * a) % m

        return sum_hash
    
    n = 15
    s1 = 0
    s2 = 0
    map = {}
    while True:
        s = generate_string(n)
        hash_s = _hash(s[::-1])
        if not map.get(hash_s):
            map[hash_s] = s
        elif map.get(hash_s) != s:
            s1 = s
            s2 = map[hash_s]
            break

    print(s1, s2)
    return str(_hash(s1[::-1]) == _hash(s2[::-1]))


def task_C(test=None):
    a, s, m, cnt = [None] * 4
    def _hash(a, m, s):
        sum_hash = 0
        pow_a_n = 1
        for char in s:
            sum_hash = (sum_hash + ord(char) * pow_a_n) % m
            pow_a_n = (pow_a_n * a) % m

        return sum_hash

    response = []
    if test:
        a = int(test[0])
        m = int(test[1])
        s = test[2]
        cnt = int(test[3])
        for c in test[4:]:
            l, r = c.split(' ')
            response.append(str(_hash(a, m, reversed(s[int(l)-1:int(r)]))))
    else:
        a = int(input())
        m = int(input())
        s = input()
        for _ in range(int(input())):
            l, r = input().split()
            response.append(str(_hash(a, m, reversed(s[int(l)-1:int(r)]))))
    
    return response


def task_D(test=None):
    def _hash(s, a=1000, m=123_987_123):
        sum_hash = 0
        pow_a_n = 1
        for i, char in enumerate(s):
            sum_hash = (sum_hash + ord(char) * pow_a_n) % m
            pow_a_n = (pow_a_n * a) % m

        return sum_hash

    hash_resp = {}
    response = []
    if test:
        n = int(test[0])
        for s in test[1:]:
            h = _hash(s)
            if not hash_resp.get(h):
                hash_resp[h] = 1
                response.append(s)
    else:
        for _ in range(int(input())):
            s = input()
            h = _hash(s)
            if not hash_resp.get(h):
                hash_resp[h] = 1
                print(s)

    return response


def task_E(test=None):
    s = None

    if test:
        s = test
    else:
        s = input()
    
    max_s = ''
    max_n = n = 1
    l, r = 0, len(s)-1
    while l <= r:
        if s[l] not in max_s:
            max_s += s[l]
            n += 1
        else:
            i = max_s.index(s[l])
            max_s = max_s[i + 1:] + s[l]
            n = len(max_s)

        max_n = n if n > max_n else max_n
        l += 1
    print(max_n)
    return str(max_n)

test_func(task_E)
