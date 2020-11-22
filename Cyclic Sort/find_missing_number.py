"""
Find the Missing Number:
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
 Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
"""


def find_missing_number(nums):

    idx = 0
    while idx < len(nums):
        # place numbers at their correct index and skipthose that can't
        if nums[idx] != idx and nums[idx] < len(nums):
            # place the current number (nums[idx]) at it's correct index (nums[nums[idx]])
            nums[nums[idx]], nums[idx] = nums[idx], nums[nums[idx]]
        else:
            idx += 1

    # find the first number missing from its index, that will be our required number
    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return -1


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()

"""
SOLUTION:
This problem follows the Cyclic Sort pattern.
Since the input array contains unique numbers from the range 0 to ‘n’, we can use a similar strategy as discussed in Cyclic Sort to place the numbers on their correct index.
Once we have every number in its correct place, we can iterate the array to find the index which does not have the correct number, and that index will be our missing number.

However, there are two differences with Cyclic Sort:

    1.In this problem, the numbers are ranged from ‘0’ to ‘n’, compared to ‘1’ to ‘n’ in the Cyclic Sort. This will make two changes in our algorithm:
        In this problem, each number should be equal to its index, compared to index + 1 in the Cyclic Sort. 
        Therefore => nums[i] == nums[nums[i]]
    2.Since the array will have ‘n’ numbers, which means array indices will range from 0 to ‘n-1’. 
      Therefore, we will ignore the number ‘n’ as we can’t place it in the array, so => nums[i] < nums.length
        Say we are at index i. If we swap the number at index i to place it at the correct index, we can still have the wrong number at index i.
        This was true in Cyclic Sort too. It didn’t cause any problems in Cyclic Sort as over there, we made sure to place one number at its correct place in each step,
         but that wouldn’t be enough in this problem as we have one extra number due to the larger range. 
        Therefore, we will not move to the next number after the swap until we have a correct number at the index i.
"""
