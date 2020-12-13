"""
Order-agnostic Binary Search

Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
"""


def binary_search(arr, key):

    length = len(arr)
    left = 0
    right = length - 1

    descending = False
    if arr[left] > arr[right]:
        descending = True

    while left <= right:
        if arr[left] == key:
            return left
        elif arr[right] == key:
            return right

        middle = (right + left) // 2

        if not descending:
            if key >= arr[middle]:
                if left == middle:
                    left = middle + 1
                else:
                    left = middle
            else:
                if right == middle:
                    right = middle - 1
                else:
                    right = middle
        # descending
        else:
            if key <= arr[middle]:
                if left == middle:
                    left = middle + 1
                else:
                    left = middle
            else:
                if right == middle:
                    right = middle - 1
                else:
                    right = middle

    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))
    print(binary_search([10, 9, 8, 6, 4, 2, 1], 4))
    print(binary_search([10, 9, 8, 6, 4, 2, 1], 2))
    print(binary_search([10, 9, 8, 6, 4, 2, 1], 9))
    print(binary_search([4, 6, 10], 20))
    print(binary_search([10, 9, 6, 8, 4], 7))


main()
