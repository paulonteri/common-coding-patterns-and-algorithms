"""
Kth Smallest Number
"""
import heapq


def find_Kth_smallest_number2(nums, k):

    heapq.heapify(nums)

    pos = 1
    while pos <= k:

        if pos == k:
            return heapq.heappop(nums)

        heapq.heappop(nums)
        pos += 1

    return -1


# we will negate all numbers and look for the kth largest number instead
def find_Kth_smallest_number(nums, k):
    heap = []

    # put first k numbers into the heap
    for i in range(k):
        heapq.heappush(heap, -nums[i])

    # remember that in the heap(min-heap), the no. at the top will always be the smallest in the heap
    #  and this case, because the heap will always have k elements,
    #   the number at the top, index 0,  will be the kth largest(and smallest), the rest will be larger than it

    # go through the remaining numbers of the array, if the number from the array is bigger than the
    # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
    #  this ensures the heap will always have the largest k values of the (negated) array
    for i in range(k, len(nums)):
        if -nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, -nums[i])

    # the root of the heap has the Kth smallest number
    return -heap[0]


def main():

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number2([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number2([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number2([5, 12, 11, -1, 12], 3)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
