"""
K-th smallest element using python heapq library

@samarjit_debnath
"""



import heapq


def k_th_smallest(a, k):
    smallest = []
    for value in a:
        if len(smallest) < k:
            heapq.heappush(smallest, -value)
        else:
            heapq.heappushpop(smallest, -value)
    if len(smallest) < k:
        return None
    return -smallest[0]


if __name__ == '__main__':
    test = int(input())
    for i in range(0, test):
        n = int(input())
        arr = map(int, input().split())
        x = int(input())
        print(k_th_smallest(arr, x))