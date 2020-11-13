"""
Triplet Sum to Zero:
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""


def search_triplets(arr):
    triplets = []
    # sort the array to help us skip duplicates plus,
    # for a given index the other two required numbers will always be infront of it (index + number)
    arr.sort()
    prev = None
    for idx in range(len(arr)):
        # for each num in the array (skipping duplicates),
        #  find the other two numbers
        if arr[idx] != prev:
            find_pair(triplets, arr, 0-arr[idx], idx)
            prev = arr[idx]
    return triplets


def find_pair(triplets, arr, req_sum, curr_idx):

    # having the left pointer just after the curr_idx will prevent double work and,
    #  prevent getting duplicates
    left = curr_idx + 1  # the two numbers will always be after the curr_idx
    right = len(arr) - 1

    while left <= right:
        total = arr[left] + arr[right]

        if total < req_sum:
            left += 1
        elif total > req_sum:
            right -= 1

        else:
            triplets.append([arr[curr_idx], arr[left], arr[right]])
            left += 1
            right -= 1


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2, 0, 0]))
    print(search_triplets([-5, 2, -1, -2, 3]))
    print(search_triplets([-5, -1, -1, 2]))


main()

"""
SOLUTION:
This problem follows the Two Pointers pattern and shares similarities with Pair with Target Sum. 
A couple of differences are that the input array is not sorted and instead of a pair we need to find triplets with a target sum of zero.
To follow a similar approach, first, we will sort the array and then iterate through it taking one number at a time. Let’s say during our iteration we are at number ‘X’,
 so we need to find ‘Y’ and ‘Z’ such that X + Y + Z == 0X+Y+Z==0. At this stage, our problem translates into finding a pair whose sum is equal to “-X−X” (as from the above equation Y + Z == -XY+Z==−X).
Another difference from Pair with Target Sum is that we need to find all the unique triplets.
 To handle this, we have to skip any duplicate number. Since we will be sorting the array, so all the duplicate numbers will be next to each other and are easier to skip.
"""
