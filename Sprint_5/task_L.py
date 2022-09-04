def sift_down(heap: [], index: int) -> int:
    left = 2 * index
    right = 2 * index + 1
    
    if len(heap) < left:
        return index

    if (right <= len(heap)) and (heap[left] < heap[right]):
        index_largest = right
    else:
        index_largest = left

    if heap[index] < heap[index_largest]:
        heap[index], heap[index_largest] = heap[index_largest], heap[index]
        return sift_down(heap, index_largest)

    return 1



# def tests():
#     tt = [
#         [[-1, 12, 1, 8, 3, 4, 7], 2, 5]
#     ]
#     for n_test in range(len(tt)):
#         test(n_test + 1, *tt[n_test])


# class bcolors:
#     OKGREEN = '\033[92m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'


# def test(n_test, sample, idx, answer):
#     isTested = sift_down(sample, idx) == answer
#     print(f"test {n_test} is {bcolors.OKGREEN if isTested else bcolors.FAIL}{isTested} {bcolors.ENDC}")


# tests()
