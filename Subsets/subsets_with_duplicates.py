"""
Subsets With Duplicates:
Given a set of numbers that might contain duplicates, find all of its distinct subsets.
Example 1:
    Input: [1, 3, 3]
    Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:
    Input: [1, 5, 3, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
"""


def find_subsets(nums):
    subsets = []

    if len(nums) < 1:
        return subsets
    nums.sort()
    subsets.append([nums[0]])

    idx = 1
    # used to mark the idx where the non duplicate subsets started being added
    last_added_start = None
    while idx < len(nums):

        # non duplicates
        if nums[idx] != nums[idx-1]:

            curr_len = len(subsets)
            for i in range(curr_len):
                arr = list(subsets[i])
                arr.append(nums[idx])
                subsets.append(arr)

            subsets.append([nums[idx]])
            last_added_start = idx

        # duplicates
        else:
            # current and the previous elements are same so we,
            #  create new subsets only from the subsets added in the previous step: start from `last_added_start`
            curr_len = len(subsets)
            while last_added_start < curr_len:
                arr = list(subsets[last_added_start])
                arr.append(nums[idx])
                subsets.append(arr)
                last_added_start += 1

        idx += 1

    return subsets


def find_subsets2(nums):
    # sort the numbers to handle duplicates
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        # if current and the previous elements are same, create new subsets only from the subsets
        # added in the previous step
        if i > 0 and nums[i] == nums[i - 1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex+1):
            # create a new subset from the existing subset and add the current element to it
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets2([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets2([1, 5, 3, 3])))


main()

"""
SOLUTION:
This problem follows the Subsets pattern and we can follow a similar Breadth First Search (BFS) approach.
The only additional thing we need to do is handle duplicates. 
Since the given set can have duplicate numbers, if we follow the same approach discussed in Subsets,
 we will end up with duplicate subsets, which is not acceptable. To handle this, we will do two extra things:

    1. Sort all numbers of the given set. This will ensure that all duplicate numbers are next to each other.
    2. Follow the same BFS approach but whenever we are about to process a duplicate (i.e., when the current and the previous numbers are same),
        instead of adding the current number (which is a duplicate) to all the existing subsets, only add it to the subsets which were created in the previous step.


Time complexity #
Since, in each step, the number of subsets doubles (if not duplicate) as we add each element to all the existing subsets,
 therefore, we will have a total of O(2^N)O(2N) subsets, where ‘N’ is the total number of elements in the input set. And since we construct a new subset from an existing set,
  therefore, the time complexity of the above algorithm will be O(N*2^N)O(N∗2N).

Space complexity #
All the additional space used by our algorithm is for the output list.
Since, at most, we will have a total of O(2^N)O(2N) subsets, and each subset can take up to O(N)O(N) space,
 therefore, the space complexity of our algorithm will be O(N*2^N)O(N∗2N).
"""
