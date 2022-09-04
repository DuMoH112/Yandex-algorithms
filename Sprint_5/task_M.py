def sift_up(heap: [], index: int) -> int:
    if index == 1:
        return 1
    parent_index = index // 2

    if heap[parent_index] < heap[index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        return sift_up(heap, parent_index)

    return index


# def tests():
#     tt = [
#         [[-1, 12, 6, 8, 3, 15, 7], 5, 1],
#     ]
#     for n_test in range(len(tt)):
#         test(n_test + 1, *tt[n_test])


# class bcolors:
#     OKGREEN = '\033[92m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'


# def test(n_test, sample, idx, answer):
#     isTested = sift_up(sample, idx) == answer
#     print(f"test {n_test} is {bcolors.OKGREEN if isTested else bcolors.FAIL}{isTested} {bcolors.ENDC}")


# tests()
