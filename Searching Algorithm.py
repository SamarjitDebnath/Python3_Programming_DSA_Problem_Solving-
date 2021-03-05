"""
Searching Algorithms

Array: 20, 40, 30, 87, 98, 100
Find Element: 30
 ----->Element found at location: 3
    .....({Array index + 1} = {2 + 1} = 3)
Find Element: 10
 -----> Item Not Found

@samarjit_debnath
"""



""" Linear Search Algorithm
Time Complexity: O(n)"""


def linear_search(array, key):
    n = len(array)
    for i in range(n):
        if array[i] == key:
            return 'Linear Search: Item found at {}'.format(i+1)

    return 'Item not found'


""" Binary Search for sorted array 
Iterative form 
Time Complexity: O(log2(n))"""


def binary_search_iterative(array, key):
    array.sort()
    n = len(array)
    low = 0
    up = n-1
    mid = (low + up) // 2

    for i in range(n):
        if key < mid:
            up = mid - 1
        else:
            low = mid + 1
        mid = (low + up) // 2
        if array[mid] == key:
            return 'Binary Search Iterative: Item found at {}'.format(mid+1)
    return 'Item not found'


""" Binary Search for sorted array 
Recursive form 
Time Complexity: O(log2(n)) """


def binary_search_recursive(array, key, low, up):
    array.sort()
    if low > up:
        return 'Item not found'
    else:
        mid = (low + up) // 2
        if key == array[mid]:
            return 'Binary Search Recursive: Item found at {}'.format(mid+1)
        elif key < mid:
            return binary_search_recursive(array, key, low, mid-1)
        else:
            return binary_search_recursive(array, key, mid+1, up)


if __name__ == '__main__':
    n = int(input('No. of Element: '))
    array = list(map(int, input('*For Binary search enter in sorted order*\nEnter Element: ').split()))[:n]
    key = int(input('Item to be searched: '))

    result0 = linear_search(array, key)
    print(result0)

    result1 = binary_search_iterative(array, key)
    print(result1)

    result2 = binary_search_recursive(array, key, 0, n-1)
    print(result2)


