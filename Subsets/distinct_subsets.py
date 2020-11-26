"""
Subsets:
Given a set with distinct elements, find all of its distinct subsets.

Example 1:
    Input: [1, 3]
    Output: [], [1], [3], [1,3]
    
Example 2:
    Input: [1, 5, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""


def find_subsets(nums):
    subsets = []

    for number in (nums):
        # we will take all existing subsets and insert the current number in them to create new subsets
        for idx in range(len(subsets)):
            # create a new subset from the existing subset and insert the current element to it
            # arr = subsets[i] # gives wrong answer
            arr = list(subsets[idx])
            arr.append(number)
            subsets.append(arr)

        subsets.append([number])

    return subsets


def main():

    print(
        "For [1, 3] , here is the list of subsets: " + str(find_subsets([1, 3])))
    print(
        "For [1, 5, 3] , here is the list of subsets " + str(find_subsets([1, 5, 3])))


main()

"""
SOLUTION:
To generate all subsets of the given set, we can use the Breadth First Search (BFS) approach.
We can start with an empty set, iterate through all numbers one-by-one, and add them to existing sets to create new subsets.

Let’s take an example to go through each step of our algorithm:
    Given set: [1, 5, 3]

    Start with an empty set: [[]]
    Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
    Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
    Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].
"""
