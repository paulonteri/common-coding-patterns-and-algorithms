"""
Top 'K' Numbers

Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
"""

import heapq


def find_k_largest_numbers2(nums, k):
    # print("    Result should be: ", heapq.nlargest(k, nums))
    result = []

    new_nums = []
    for num in nums:
        heapq.heappush(new_nums, -num)

    while k > 0:
        result.append(-heapq.heappop(new_nums))
        k -= 1

    return result


def find_k_largest_numbers(nums, k):
    minHeap = []
    # put first 'K' numbers in the min heap
    for i in range(k):
        heapq.heappush(minHeap, nums[i])

    # go through the remaining numbers of the array, if the number from the array is bigger than the
    # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, nums[i])

    # the heap has the top 'K' numbers, return them in a list
    return list(minHeap)


def main():

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers2([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers2([5, 12, 11, -1, 12], 3)))


main()
