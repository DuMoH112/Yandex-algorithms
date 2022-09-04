from time import time


def test(func, idx: int, answer: any, arguments: [], response=None, start_t=0, end_t=0):
    if not response:
        start_t = time()
        response = func(*arguments)
        end_t = time()
    isTested = response == answer
    print(f"""     
Test {idx + 1} is {bcolors.OKGREEN if isTested else bcolors.FAIL} {isTested} {bcolors.ENDC}
Time done: {"{:.7f}".format(end_t - start_t)}
""")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
