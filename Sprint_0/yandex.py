def task_A():
    a = int(input())
    b = int(input())
    print(a + b)


def task_B():
    count_elements = int(input())
    list_1 = input().split(" ")
    list_2 = input().split(" ")
    print(
        " ".join([f"{list_1[i]} {list_2[i]}" for i in range(count_elements)]))


def task_C(count_elements, timeseries, K):
    # count_elements = int(input())
    # timeseries = [int(i) for i in input().split(" ")]
    # K = int(input())

    current_sum = sum(timeseries[:K])
    result = [str(current_sum / K)]
    for i in range(len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        result.append(str(current_sum / K))
    print(" ".join(result))


def task_D(count_elements, numbers, X):
    # count_elements = int(input())
    # numbers = [int(i) for i in input().split(" ")]
    # X = int(input())

    def main(numbers, X):
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == X:
                    return f"{numbers[i]} {numbers[j]}"
        else:
            return f"{None}"

    print(main(numbers, X))


def task_D_2(count_elements, numbers, X):
    # count_elements = int(input())
    # numbers = [int(i) for i in input().split(" ")]
    # X = int(input())

    def main(numbers, X):
        numbers.sort()
        left = 0
        right = len(numbers) - 1
        while left < right:
            print
            current_sum = numbers[left] + numbers[right]
            if current_sum == X:
                return f"{numbers[left]} {numbers[right]}"
            elif current_sum < X:
                left += 1
            else:
                right -= 1

        return f"{None}"
    print(main(numbers, X))


def task_D_3(count_elements, numbers, X):
    # count_elements = int(input())
    # numbers = [int(i) for i in input().split(" ")]
    # X = int(input())

    def main(numbers, X):
        previous = set()
        for A in numbers:
            Y = X - A
            if Y in previous:
                return f"{A} {Y}"
            else:
                previous.add(A)

        return f"{None}"
    print(main(numbers, X))

tests = [
    [8, "6 2 8 -3 1 1 6 10", 100],
    [10, "-96 -93 -39 -30 -11 11 22 40 67 84", -186]
]

for test in tests:
    count_elements, numbers, X = test
    numbers = [int(i) for i in numbers.split(" ")]
    task_D_3(count_elements, numbers, X)
