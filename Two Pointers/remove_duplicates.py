"""
Remove Duplicates:
Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space;
 after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
"""


# Remember the array will be sorted.
# This means that duplicates will be right next to each other
def remove_duplicates(arr):
    length = len(arr)
    if length < 2:
        return length

    # move these two pointers together,
    # replacing the value at the after_none_duplicate with the value at curr
    # but let the after_none_duplicate stick after spotting a duplicate, till we...
    # find a different, non-duplicate value, from the curr pointer and replace it with it
    curr = 1
    after_none_duplicate = 1
    while curr < length:
        # if not duplicate continue with the process of
        #  replacing the after_none_duplicate with the value at curr
        #  and moving the pointer forward
        if arr[after_none_duplicate - 1] != arr[curr]:
            arr[after_none_duplicate] = arr[curr]
            after_none_duplicate += 1
            curr += 1
        else:
            curr += 1
    return after_none_duplicate


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()

"""
SOLUTION:
We need to remove the duplicates in-place such that the resultant length of the array remains sorted. 
As the input array is sorted, therefore, one way to do this is to shift the elements left whenever we encounter duplicates.
In other words, we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number.
So our algorithm will be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we’ve seen.
"""
