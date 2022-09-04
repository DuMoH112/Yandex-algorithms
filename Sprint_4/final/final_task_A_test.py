import os
import sys
import time

from final_task_A import search_in_query, create_index

sys.path.append(os.getcwd())
from tools import test

praktikum_tests = [
    {"test": [
        "3",
        "i like dfs and bfs",
        "i like dfs dfs",
        "i like bfs with bfs and bfs",
        "1",
        "dfs dfs dfs dfs bfs",
    ], "answer": [
        "3 1 2"
    ]},
    {"test": [
        "3",
        "i love coffee",
        "coffee with milk and sugar",
        "free tea for everyone",
        "3",
        "i like black coffee without milk",
        "everyone loves new year",
        "mary likes black coffee without milk",
    ], "answer": [
        "1 2",
        "3",
        "2 1",
    ]},
    {"test": [
        "6",
        "buy flat in moscow",
        "rent flat in moscow",
        "sell flat in moscow",
        "want flat in moscow like crazy",
        "clean flat in moscow on weekends",
        "renovate flat in moscow",
        "1",
        "flat in moscow for crazy weekends",
    ], "answer": [
        "4 5 1 2 3"
    ]},
    {"test": [
        "10",
        "tjegerxbyk pdvmj wulmqfrx",
        "pndygsm dvjihmxr tcdtqsmfe",
        "txamzxqzeq dxkxwq aua",
        "hsciljsrdo fipazun kngi",
        "xtkomk aua wulmqfrx ydkbncmzee",
        "pndygsm cqvffye pyrhcxbcef",
        "szyc uffqhayg ccktodig",
        "ntr wpvlifrgjg htywpe",
        "kngi tjegerxbyk zsnfd",
        "tqilkkd gq qc fipazun",
        "5",
        "dxkxwq htywpe",
        "aua tjegerxbyk",
        "xtkomk tjegerxbyk",
        "szyc fipazun",
        "xtkomk tjegerxbyk",
    ], "answer": [
        "3 8",
        "1 3 5 9",
        "1 5 9",
        "4 7 10",
        "1 5 9",
    ]},
    {"test": [
        "10",
        "dvuceyw fmb hwmmg klloy",
        "fcti mnbu mbhrw txuxi",
        "yrxbjm ntkhau yfg lza",
        "jjmnqoz mamrxrxof gk",
        "ksmhly gijsrqihf veal",
        "hlqi moepw irjkylno fcti",
        "ouue fmb hlqi gijsrqihf",
        "ntkhau twzgbh uugtkfswv",
        "zquzvlk gijsrqihf eyga",
        "hwmmg cb ajfujbdn szbgwc",
        "5",
        "dvuceyw txuxi",
        "hlqi hwmmg",
        "lza uugtkfswv",
        "ajfujbdn fmb",
        "klloy drm uugtkfswv",
    ], "answer": [
        "1 2",
        "1 6 7 10",
        "3 8",
        "1 7 10",
        "1 8",
    ]}
]


if __name__ == '__main__':
    for idx, row in enumerate(praktikum_tests):
        cnt_docs = int(row['test'][0])
        indexes = {}
        for id, string in enumerate(row['test'][1:cnt_docs+1]):
            id += 1
            create_index(indexes, id, string)

        cnt_query = int(row['test'][cnt_docs+1])

        result = []
        start_t = time.time()
        for query in row['test'][cnt_docs+2:cnt_docs+2+cnt_query]:
            result.append(search_in_query(query, indexes))
        end_t = time.time()

        test(None, idx, row['answer'], None, result, start_t=start_t, end_t=end_t)
