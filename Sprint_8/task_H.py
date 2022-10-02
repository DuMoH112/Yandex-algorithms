import os
import sys

sys.path.append(os.getcwd())
from tools import test


def all_replace(string: str, find: str, replace:str):
    return string.replace(find, replace)


def main():
    string = input()
    find = input()
    replace = input()
    print(all_replace(string, find, replace))


tests = [
    {"test": [
        'pingpong',
        'ng',
        'mpi',
    ], "answer": "pimpipompi"},
    {"test": [
        'aaa',
        'a',
        'ab',
    ], "answer": "ababab"},
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        string = row['test'][0]
        find = row['test'][1]
        replace = row['test'][2]
        test(all_replace, idx, row['answer'], [string, find, replace])
