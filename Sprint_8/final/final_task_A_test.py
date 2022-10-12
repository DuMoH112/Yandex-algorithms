import os
import sys

from final_task_A import unpack, max_prefix

sys.path.append(os.getcwd())
from tools import test

praktikum_tests = [
    {"test": [
        '3',
        '2[a]2[ab]',
        '3[a]2[r2[t]]',
        'a2[aa3[b]]',
    ], "answer": 'aaa'},
    {"test": [
        '3',
        'abacabaca',
        '2[abac]a',
        '3[aba]',
    ], "answer": 'aba'},
]


if __name__ == '__main__':
    for idx, row_t in enumerate(praktikum_tests):
        cnt_str = row_t['test'][0]
        
        prefix = unpack(row_t['test'][1])
        for row in row_t['test'][2:]:
            prefix = max_prefix(prefix, unpack(row))

        test(None, idx, row_t['answer'], None, prefix)
