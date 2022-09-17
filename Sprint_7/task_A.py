import os
import sys
import time

sys.path.append(os.getcwd())
from tools import test


def exchange(days_cnt, stock_prices):
    overall_benefit = 0
    for i in range(1, days_cnt):
        if stock_prices[i-1] < stock_prices[i]:
            overall_benefit += (stock_prices[i] - stock_prices[i-1])
        
    return overall_benefit


def main():
    days_cnt = int(input())
    stock_prices = [int(v) for v in input().split(' ')]
    print(exchange(days_cnt, stock_prices))


tests = [
    {"test": [
        "6",
        "7 1 5 3 6 4",
    ], "answer": 7},
    {"test": [
        "5",
        "1 2 3 4 5",
    ], "answer": 4},
    {"test": [
        "6",
        "1 12 12 16 1 8",
    ], "answer": 22},
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        days_cnt = int(row['test'][0])
        stock_prices = [int(v) for v in row['test'][1].split(' ')]

        test(exchange, idx, row['answer'], [days_cnt, stock_prices])
