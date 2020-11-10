"""
Given an array of positive numbers and a positive number ‘S,’ 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0 if no such subarray exists.
"""


def smallest_subarray_with_given_sum(s, arr):
    smallest_len = float('inf')  # smallest length we have found so far

    curr_sum = 0  # window sum
    left, right = 0, 0  # pointers
    while right < len(arr):
        curr_sum += arr[right]

        while curr_sum >= s and left <= right:
            smallest_len = min(smallest_len, (right-left+1))
            # make window smaller
            curr_sum -= arr[left]
            left += 1

        right += 1

    # if it is still the default value, return 0
    if smallest_len == float('inf'):
        return 0
    return smallest_len


"""
SOLUTION:
First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to ‘S.’
These elements will constitute our sliding window. We are asked to find the smallest such window having a sum greater than or equal to ‘S.’ We will remember the length of this window as the smallest window so far.
After this, we will keep adding one element in the sliding window (i.e., slide the window ahead) in a stepwise fashion.
In each step, we will also try to shrink the window from the beginning. We will shrink the window until the window’s sum is smaller than ‘S’ again. This is needed as we intend to find the smallest window. This shrinking will also happen in multiple steps; in each step, we will do two things:
Check if the current window length is the smallest so far, and if so, remember its length.
Subtract the first element of the window from the running sum to shrink the sliding window.
"""
