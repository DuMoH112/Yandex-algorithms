from time import time


def test_func(func):
    tests = {
        "task_A": [
            {"test": "-8 -5 -2 7", "answer": -183},
            {"test": "8 2 9 -10", "answer": 40}
        ],
        "task_B": [
            {"test": "1 2 -3", "answer": "FAIL"},
            {"test": "7 11 7", "answer": "WIN"},
            {"test": "6 -2 0", "answer": "WIN"}
        ],
        "task_C": [
            {"test": ["4", "3", "1 2 3", "0 2 6", "7 4 1",
                      "2 7 0", "3", "0"], "answer": "7 7"},
            {"test": ["4", "3", "1 2 3", "0 2 6", "7 4 1",
                      "2 7 0", "0", "0"], "answer": "0 2"}
        ],
        "task_D": [
            {"test": ["7", "-1 -10 -8 0 2 0 5"], "answer": 3},
            {"test": ["5", "1 2 5 4 8"], "answer": 2},
            {"test": ["1", "-133"], "answer": 1}
        ],
        "task_E": [
            {"test": ["19", "i love segment tree"], "answer": ["segment", 7]},
            {"test": ["21", "frog jumps from river"], "answer": ["jumps", 5]},
        ],
        "task_F": [
            {"test": "A man, a plan, a canal: Panama", "answer": True},
            {"test": "zo", "answer": False}
        ],
        "task_G": [
            {"test": "5", "answer": 101},
            {"test": "14", "answer": 1110}
        ],
        "task_H": [
            {"test": ["1010", "1011"], "answer": 10101},
            {"test": ["1", "1"], "answer": 10},
            {"test": ["11001", "1"], "answer": 11010}
        ],
        "task_I": [
            {"test": "15", "answer": False},
            {"test": "16", "answer": True},
            {"test": "1", "answer": False}
        ],
        "task_J": [
            {"test": "8", "answer": "2 2 2"},
            {"test": "13", "answer": "13"},
            {"test": "100", "answer": "2 2 5 5"},
            {"test": "3", "answer": "3"}
        ],
        "task_K": [
            {"test": ["4", "1 2 0 0", "34"], "answer": "1 2 3 4"},
            {"test": ["2", "9 5", "17"], "answer": "1 1 2"},
        ],
        "task_D": [
            {"test": ["abcd", "abcde"], "answer": "e"},
            {"test": ["go", "ogg"], "answer": "g"},
            {"test": ["xtkpx", "xkctpx"], "answer": "c"},
        ],
        "task_Final_1": [
            {"test": ["8", "0 7 9 0 8 20 11 0"], "answer": "0 1 1 0 1 2 1 0"},
            {"test": ["9", "0 0 7 9 0 0 8 20 0"],
                "answer": "0 0 1 1 0 0 1 1 0"},
            {"test": ["6", "5 0 1 4 9 0"], "answer": "1 0 1 2 1 0"},
            {"test": ["5", "0 1 4 9 0"], "answer": "0 1 2 1 0"},
            {"test": ["6", "0 7 9 4 8 20"], "answer": "0 1 2 3 4 5"},
            {"test": ["1", "0"], "answer": "0"},
            {"test": ["4", "0 0 0 0"], "answer": "0 0 0 0"},
            {"test": ["7", "87 7 9 4 8 20 0"], "answer": "6 5 4 3 2 1 0"},
            {
                "test": ["1000000", f'1 {" ".join("0" for i in range(1000000 - 1))}'],
                "answer": f'1 {" ".join("0" for i in range(1000000 - 1))}'
            },
        ],
        "task_Final_2": [
            {
                "test": [
                    "3",
                    "1231",
                    "2..2",
                    "2..2",
                    "2..2",
                ],
                "answer": "2"
            },
            {
                "test": [
                    "4",
                    "1111",
                    "9999",
                    "1111",
                    "9911",
                ],
                "answer": "1"
            },
            {
                "test": [
                    "4",
                    "1111",
                    "1111",
                    "1111",
                    "1111",
                ],
                "answer": "0"
            },
        ],
    }

    for index, row in enumerate(tests[func.__name__]):
        start_t = time()
        response = func(row['test'])
        end_t = time()
        print(f"""     
Test {index + 1} is {response == row['answer']}
Time done: {"{:.7f}".format(end_t - start_t)}
""")

    return


def task_A(test=None):
    a, x, b, c = None
    if test:
        a, x, b, c = [int(i) for i in test.split(' ')]
    else:
        a, x, b, c = [int(i) for i in input().split(' ')]

    return a*x*x + b*x + c


def task_B(test=None):
    numbers = None
    if test:
        numbers = [int(i) for i in test.split(' ')]
    else:
        numbers = [int(i) for i in input().split(' ')]

    result = [True for num in numbers if num % 2 == 0]
    result = "WIN" if len(result) == 3 or len(result) == 0 else "FAIL"
    return result


def task_C(test=None):
    n, m, matrix, find_n, find_m = [None]*5
    if test:
        n = int(test[0])
        m = int(test[1])
        matrix = [[int(num) for num in line.split(' ')] for line in test[2:-2]]
        find_n = int(test[-2])
        find_m = int(test[-1])
    else:
        n = int(input())
        m = int(input())
        matrix = [[int(num) for num in input().split(' ')]
                  for line in range(n)]
        find_n = int(input())
        find_m = int(input())

    left = matrix[find_n][find_m - 1] if find_m > 0 else None
    right = matrix[find_n][find_m + 1] if find_m < (m - 1) else None
    top = matrix[find_n - 1][find_m] if find_n > 0 else None
    bottom = matrix[find_n + 1][find_m] if find_n < (n - 1) else None

    result = [i for i in [left, right, top, bottom] if i != None]
    result.sort()
    result = " ".join(str(i) for i in result)

    return result


def task_D(test=None):
    n, temps = [None]*2
    if test:
        n = int(test[0])
        temps = [int(num) for num in test[1].split(' ')]
    else:
        n = int(input())
        temps = [int(num) for num in input().split(' ')]

    if len(temps) > 1:
        result = (temps[0] > temps[1]) + (temps[n-1] > temps[n-2])
        for day in range(1, n-1):
            if (temps[day] > temps[day-1]) and (temps[day] > temps[day+1]):
                result += 1
        print(result)
        return result
    else:
        return 1


def task_E(test=None):
    if test:
        n = int(test[0])
        words = test[1].split(' ')
    else:
        n = int(input())
        words = input().split(' ')

    max_len = len(words[0])
    max_word = words[0]

    if len(words) > 1:
        for word in words[1:]:
            len_word = len(word)
            if len_word > max_len:
                max_len = len_word
                max_word = word

    print(max_word)
    print(max_len)

    return [max_word, max_len]


def task_F(test=None):
    string = None
    if test:
        string = test
    else:
        string = input()

    def search_palindrom(string):
        cursor_start = 0
        cursor_end = len(string) - 1

        while cursor_start < len(string) - 1:
            if not string[cursor_start].isalpha():
                cursor_start += 1
                continue
            if not string[cursor_end].isalpha():
                cursor_end -= 1
                continue

            if string[cursor_start].lower() != string[cursor_end].lower():
                return False

            cursor_start += 1
            cursor_end -= 1

        return True

    result = search_palindrom(string)
    print(search_palindrom(string))
    return result


def task_G(test=None):
    number = None
    if test:
        number = int(test)
    else:
        number = int(input())

    result = ""
    while number > 0:
        if number % 2 == 0:
            result += "0"
        else:
            result += "1"

        number = number // 2

    result = result[::-1]
    print(result)
    return int(result)


def task_H(test=None):
    if test:
        number_1 = test[0][::-1]
        number_2 = test[1][::-1]
    else:
        number_1 = input()[::-1]
        number_2 = input()[::-1]

    result = ""
    max_len = max(len(number_1), len(number_2))
    overflow = 0

    number_1 += "0" * (max_len - len(number_1))
    number_2 += "0" * (max_len - len(number_2))

    for num_1, num_2 in zip(number_1, number_2):
        summ = int(num_1) + int(num_2) + overflow
        overflow = summ // 2
        result += str(summ % 2)

    if overflow:
        result += str(overflow)

    print(result[::-1])
    return int(result[::-1])


def task_I(test=None):
    if test:
        number = int(test)
    else:
        number = int(input())

    def isSqrFour(number):
        if number == 1:
            return True
        sqr = 4
        while sqr <= number:
            if sqr == number:
                return True
            sqr *= 4

        return False

    print(isSqrFour(number))
    return isSqrFour(number)


def task_J(test=None):
    if test:
        number = int(test)
    else:
        number = int(input())

    def factorsation(number: int):
        simple_number = 2
        primary_nimbers = []
        while simple_number * simple_number <= number:
            while number % simple_number == 0:
                primary_nimbers.append(simple_number)
                number = number / simple_number
            simple_number = simple_number + 1
        if number > 1:
            primary_nimbers.append(int(number))
        return " ".join(str(i) for i in primary_nimbers)

    print(factorsation(number))
    return factorsation(number)


def task_K(test=None):
    if test:
        x = int(test[0])
        list_forma = test[1].split(' ')
        k = int(test[2])
    else:
        x = int(input())
        list_forma = input().split(' ')
        k = int(input())

    list_forma = int("".join(list_forma))

    result = " ".join(i for i in str(list_forma+k))

    print(result)
    return result


def task_D(test=None):
    if test:
        s = test[0]
        t = test[1]
    else:
        s = input()
        t = input()

    dict_ = {}
    for i in s:
        if dict_.get(i):
            dict_[i] += 1
            continue
        dict_[i] = 1

    def search_for_an_extra_char(t):
        for i in t:
            if dict_.get(i) and dict_.get(i) > 0:
                dict_[i] -= 1
                continue

            return i

    result = search_for_an_extra_char(t)
    print(result)
    return result


def task_Final_1(test=None):
    n, street = None, None
    if test:
        n = int(test[0])
        street = [int(i) for i in test[1].split(' ')]
    else:
        n = int(input())
        street = [int(i) for i in input().split(' ')]

    def get_nearest_zero(n: int, street: [int]) -> str:
        indexes_of_zero = [i for i, x in enumerate(street) if x == 0]
        len_ioz = len(indexes_of_zero)
        if n == len_ioz:
            return " ".join("0" for i in range(n))

        # get distances before first zero
        if indexes_of_zero[0] != 0:
            for idx_house in range(indexes_of_zero[0]):
                street[idx_house] = indexes_of_zero[0] - idx_house

        # get distances between first and last zero
        if len_ioz > 1:
            l_idx_zero = indexes_of_zero[0]
            r_idx_zero = indexes_of_zero[1]
            idx_zero = 1
            for idx_house in range(l_idx_zero+1, indexes_of_zero[-1]):
                if street[idx_house]:
                    street[idx_house] = min(idx_house - l_idx_zero, r_idx_zero - idx_house)
                else:
                    idx_zero += 1
                    l_idx_zero = r_idx_zero
                    r_idx_zero = indexes_of_zero[idx_zero]

        # get distances after last zero
        if indexes_of_zero[-1] != n:
            for idx_house in range(indexes_of_zero[-1] + 1, n):
                street[idx_house] = idx_house - indexes_of_zero[-1]

        return street

    res = get_nearest_zero(n, street)

    return " ".join(str(i) for i in res)


def task_Final_2(test=None):
    # id package is 69051539
    k, keyboard = None, None
    if test:
        k = int(test[0])
        keyboard = [[int(j) if j != '.' else None for j in row] for row in test[1:]]
    else:
        k = int(input())
        keyboard = [[int(j) if j != '.' else None for j in input()] for _ in range(4)]

    dict_key = {}
    for row in keyboard:
        for key in row:
            if key and dict_key.get(key):
                dict_key[key] += 1
                continue
            dict_key[key] = 1

    result = 0
    for key in dict_key:
        if key and dict_key[key] <= k*2:
            result += 1
    return str(result)


test_func(task_Final_1)
