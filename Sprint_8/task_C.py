import os
import sys

sys.path.append(os.getcwd())
from tools import test


def longest_palindrom(string):
    chars = {}
    for c in string:
        chars[c] = chars.get(c, 0) + 1
    
    chars = {i: chars[i] for i in sorted(chars)}
    begin, mid = [], []
    for c in chars:
        if chars[c] % 2 == 0:
            char = c * (chars[c] // 2)
            begin.append(char)
        else:
            begin.append(c * ((chars[c] - 1) // 2))
            mid.append(c)

    mid = [mid[0]] if len(mid) > 0 else []
    response = ''.join(i for i in begin + mid + begin[::-1])
    return response


def main():
    print(longest_palindrom(input()))


tests = [
    {"test": "aaaabb", "answer": "aabbaa"},
    {"test": "pabcd", "answer": "a"},
    {"test": "aaabbb", "answer": "ababa"},
    {"test": "pabcde", "answer": "a"},
    {"test": "aaabbbe", "answer": "ababa"},
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        test(longest_palindrom, idx, row['answer'], [row['test']])
