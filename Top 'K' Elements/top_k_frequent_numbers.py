"""
Top 'K' Frequent Numbers:
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example:
    Input: [1, 3, 5, 12, 11, 12, 11], K = 2
    Output: [12, 11]
    Explanation: Both '11' and '12' apeared twice.
"""
import heapq


def find_k_frequent_numbers(nums, k):

    counter = {}
    for num in nums:
        if num in counter:
            counter[num] = counter[num] + 1
        else:
            counter[num] = 1

    heap = []
    for number, frequency in counter.items():
        heapq.heappush(heap, (frequency, number))

        # we remove the numbers with the smaller frequencies on the fly,
        #  remaining with only k items in the heap
        if len(heap) > k:
            heapq.heappop(heap)

    # create a list of top k numbers
    top_numbers = []
    while heap:
        top_numbers.append(heapq.heappop(heap)[1])

    return top_numbers


def main():

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
