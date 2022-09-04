import os
import sys

from final_task_B import performing_an_operation, HashTable

sys.path.append(os.getcwd())
from tools import test

tests = [
    {
        "test": [
            "10",
            "get 1",
            "put 1 10",
            "put 2 4",
            "get 1",
            "get 2",
            "delete 2",
            "get 2",
            "put 1 5",
            "get 1",
            "delete 2",
        ],
        "answer": [
            "None",
            "10",
            "4",
            "4",
            "None",
            "5",
            "None",
        ]
    },
    {
        "test": [
            "8",
            "get 9",
            "delete 9",
            "put 9 1",
            "get 9",
            "put 9 2",
            "get 9",
            "put 9 3",
            "get 9",
        ],
        "answer": [
            "None",
            "None",
            "1",
            "2",
            "3",
        ]
    },
]

if __name__ == '__main__':
    for idx, row in enumerate(tests):
        cnt_query = int(row['test'][0])
        response = []
        ht = HashTable(cnt_query)
        for string in row['test'][1:]:
            cmd, *kv = string.split(' ')
            res = performing_an_operation(ht, cmd, kv)
            if res != "NO":
                response.append(str(res))
        
        test(None, idx, tests[idx]['answer'], None, response)
