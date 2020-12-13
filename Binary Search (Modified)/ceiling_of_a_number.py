"""
Ceiling of a Number 

Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’.
The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.
"""


def search_ceiling_of_a_number(arr, key):
    ceiling = -1

    left = 0
    right = len(arr)-1

    if arr[right] > key:
        ceiling = right
    else:
        return ceiling

    while left <= right:
        if arr[left] == key:
            return left
        elif arr[right] == key:
            return right

        # adjust ceiling
        elif arr[left] >= key and arr[left] < arr[ceiling]:
            ceiling = left
        elif arr[right] >= key and arr[right] < arr[ceiling]:
            ceiling = right

        # split the serch area by half
        middle = (left + right) // 2
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

    return ceiling


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
