"""
Pair with Target Sum:
Given an array of sorted numbers and a target sum,
find a pair in the array whose sum is equal to the given target.
"""


def pair_with_targetsum(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while left <= right:
        total = arr[left] + arr[right]

        if total > target_sum:
            # decrease total
            right -= 1

        elif total < target_sum:
            # increase total
            left += 1

        else:
            return[left, right]

    return [-1, -1]


"""
SOLUTION:
We can follow the Two Pointers approach. We will start with one pointer pointing to the beginning of the array and another pointing at the end.
 At every step, we will see if the numbers pointed by the two pointers add up to the target sum. 
 If they do, we have found our pair; otherwise, we will do one of two things:

If the sum of the two numbers pointed by the two pointers is greater than the target sum,
 this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer.
If the sum of the two numbers pointed by the two pointers is smaller than the target sum,
 this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer.
"""
