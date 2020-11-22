"""
Find the Duplicate Number:
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.
"""


# O(n) time | O(n) space
def find_duplicate(nums):
    idx = 0
    while idx < len(nums):
        num = nums[idx]

        if num == idx + 1:
            idx += 1
        else:
            # # swap
            # place num in the correct index (num-1) then,
            # move the number that was at the correct index(num-1) to the current index(idx)
            # However, if we find a duplicate, return it
            temp_num = nums[num-1]

            if temp_num == num:
                return num
            nums[num-1] = num
            nums[idx] = temp_num

    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()

"""
Solution
This problem follows the Cyclic Sort pattern and shares similarities with Find the Missing Number.
Following a similar approach, we will try to place each number on its correct index.
Since there is only one duplicate, if while swapping the number with its index both the numbers being swapped are same,
 we have found our duplicate!
"""
