import os
import sys

sys.path.append(os.getcwd())
from tools import test


def comparison(str1: str, str2: str):
    return 0 if str1 == str2 else 1 if str1 > str2 else -1

def read_str_to_ord_list(string):
    return [ord(i) for i in string if ord(i) % 2 == 0]

def main():
    str1 = read_str_to_ord_list(input())
    str2 = read_str_to_ord_list(input())
    
    print(comparison(str1, str2))


tests = [
    {"test": [
        'gggggbbb',
        'bbef',
    ], "answer": -1},
    {"test": [
        'z',
        'aaaaaaa',
    ], "answer": 1},
    {"test": [
        'ccccz',
        'aaaaaz',
    ], "answer": 0},
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        str1 = read_str_to_ord_list(row['test'][0])
        str2 = read_str_to_ord_list(row['test'][1])

        test(comparison, idx, row['answer'], [str1, str2])
