"""
Permutations:
Given a set of distinct numbers, find all of its permutations.
Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:
    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}
If a set has ‘n’ distinct elements it will have n! permutations.

Example 1:
    Input: [1,3,5]
    Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
"""

# https://github.com/paulonteri/leetcode/blob/master/Arrays%20and%20Strings/permutations.py


from collections import deque
from typing import List


def getPermutations(nums, num):
    array_of_nums = []
    for idx in range(len(nums) + 1):
        new_arr = list(nums)
        new_arr.insert(idx, num)
        array_of_nums.append(new_arr)
    return array_of_nums


def find_permutations(nums: List[int]) -> List[List[int]]:
    result = []
    result.append([nums[0]])
    index = 1
    while index < len(nums):
        num = nums[index]

        new_result = []
        for arr in result:
            new_result += getPermutations(arr, num)

        result = new_result

        index += 1

    return result


def find_permutations2(nums):
    numsLength = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for currentNumber in nums:
        # we will take all existing permutations and add the current number to create new permutations
        n = len(permutations)
        for _ in range(n):
            oldPermutation = permutations.popleft()
            # create a new permutation by adding the current number at every position
            for j in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currentNumber)
                if len(newPermutation) == numsLength:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)

    return result


def main():
    print("Here are all the permutations: " +
          str(find_permutations([1, 3, 5])))
    print("Here are all the permutations: " +
          str(find_permutations2([1, 3, 5])))
    print("Here are all the permutations: " +
          str(find_permutations([1, 3, 5, 4])))
    print("Here are all the permutations: " +
          str(find_permutations2([1, 3, 5, 4])))


main()
