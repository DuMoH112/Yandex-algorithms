import os
import sys

sys.path.append(os.getcwd())
from tools import test


def reverse(string):
    return ' '.join(s for s in string.split(' ')[::-1])


def main():
    print(reverse(input()))


tests = [
    {"test": "one two three", "answer": "three two one"},
    {"test": "hello", "answer": "hello"},
    {"test": "may the force be with you", "answer": "you with be force the may"},
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        test(reverse, idx, row['answer'], [row['test']])
