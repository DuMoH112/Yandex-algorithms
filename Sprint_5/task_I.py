import os
import sys
import time

sys.path.append(os.getcwd())
from tools import test


def fac(n: int) -> int:
    if n == 0:
        return 1
    return fac(n-1) * n


def solution(n: int) -> int:
    # (2 * n)! / (n! * (n + 1)!) 
    return int(fac(2*n)/(fac(n)*fac(n+1)))


tests = [
    {"test": ["2"], "answer": [2]},
    {"test": ["3"], "answer": [5]},
    {"test": ["4"], "answer": [14]},
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        num = int(row['test'][0])

        start_t = time.time()
        result = solution(num)
        end_t = time.time()

        print(result)
        test(None, idx, row['answer'], None, [result], start_t=start_t, end_t=end_t)
