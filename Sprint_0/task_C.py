import os
import sys

sys.path.append(os.getcwd())
from tools import test


def moving_average(timeseries, K):
    current_sum = sum(timeseries[:K])
    result = [current_sum / K]
    for i in range(len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        result.append(current_sum / K)
    
    return ' '.join(str(i) if not i.is_integer()  else str(int(i)) for i in result)


def main():
    count_elements = int(input())
    timeseries = [int(i) for i in input().split(" ")]
    K = int(input())

    print(moving_average(timeseries, K))


def start_test():
    for idx, row in enumerate(tests):
        count_elements = int(row['test'][0])
        timeseries = [int(i) for i in row['test'][1].split(" ")]
        K = int(row['test'][2])
        test(moving_average, idx, row['answer'], [timeseries, K])

tests = [
    {"test": [
        "7",
        "1 2 3 4 5 6 7",
        "4",
    ], "answer": "2.5 3.5 4.5 5.5"},
    {"test": [
        "9",
        "9 3 2 0 1 5 1 0 0",
        "3",
    ], "answer": "4.666666666666667 1.6666666666666667 1 2 2.3333333333333335 2 0.3333333333333333"},
    {"test": [
        "5",
        "1 2 3 4 5",
        "5",
    ], "answer": "3"},
]

if __name__ == '__main__':
    start_test()
