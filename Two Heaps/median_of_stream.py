"""
Find the Median of a Number Stream:
Design a class to calculate the median of a number stream. The class should have the following two methods:
    insertNum(int num): stores the number in the class
    findMedian(): returns the median of all numbers inserted in the class
Hint: If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example:
    1. insertNum(3)
    2. insertNum(1)
    3. findMedian() -> output: 2
    4. insertNum(5)
    5. findMedian() -> output: 3
    6. insertNum(4)
    7. findMedian() -> output: 3.5
"""
import heapq


class MedianOfAStream:

    max_heap = []  # containing first half of numbers
    min_heap = []  # containing second half of numbers
    count = 0

    def insert_num(self, num):

        if not self.max_heap or num <= self.max_heap[0]:
            heapq.heappush(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, -num)

        self.count += 1

        # balance items
        if self.count > 1:
            # either both the heaps will have equal number of elements or,
            # the max-heap will have one more element than the min-heap
            if self.count % 2 == 0:
                if len(self.max_heap) > len(self.min_heap):
                    heapq.heappush(self.min_heap,
                                   -heapq.heappop(self.max_heap))
            else:
                if len(self.max_heap) - 1 > len(self.min_heap):
                    heapq.heappush(self.min_heap,
                                   -heapq.heappop(self.max_heap))

    def find_median(self):
        if not self.max_heap:
            return 0.0

        if self.count % 2 == 0:
            # we have even number of elements, take the average of middle two elements
            return (self.max_heap[0] + -self.min_heap[0]) / 2
        else:
            # because max-heap will have one more element than the min-heap
            return self.max_heap[0]


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()

"""
SOLUTION:
As we know, the median is the middle value in an ordered integer list. 
So a brute force solution could be to maintain a sorted list of all numbers inserted in the class so that we can efficiently return the median whenever required. 
Inserting a number in a sorted list will take O(N)O(N) time if there are ‘N’ numbers in the list. This insertion will be similar to the Insertion sort. 
Can we do better than this? Can we utilize the fact that we don’t need the fully sorted list - we are only interested in finding the middle element?

Assume ‘x’ is the median of a list. 
This means that half of the numbers in the list will be smaller than (or equal to) ‘x’ and half will be greater than (or equal to) ‘x’.
This leads us to an approach where we can divide the list into two halves: one half to store all the smaller numbers (let’s call it smallNumList) and one half to store the larger numbers (let’s call it largNumList).
The median of all the numbers will either be the largest number in the smallNumList or the smallest number in the largNumList.
If the total number of elements is even, the median will be the average of these two numbers.

The best data structure that comes to mind to find the smallest or largest number among a list of numbers is a Heap. 
Let’s see how we can use a heap to find a better algorithm.

We can store the first half of numbers (i.e., smallNumList) in a Max Heap. We should use a Max Heap as we are interested in knowing the largest number in the first half.
We can store the second half of numbers (i.e., largeNumList) in a Min Heap, as we are interested in knowing the smallest number in the second half.
Inserting a number in a heap will take O(logN)O(logN), which is better than the brute force approach.
At any time, the median of the current list of numbers can be calculated from the top element of the two heaps.


Divide streams into max-heap and min-heap:
    1. If number is smaller than the top(largest) of the max-heap, add it to the min-heap.
    2. if the (len(max-heap) - 1) > len(min-heap), move the top of the max-heap to the mean heap.
    3. If the number is larger then the top(smallest) of the min-heap, add it to the max-heap.
    4. if the len(min-heap) > len(max-heap), add the top of the min-heap to the max-heap.

    Note: After every insertion, what we are doing is balancing the number of elements in both heaps,
     so that they have an equal number of elements if the total count of numbers is even or the max-heap can have (len(min-heap) + 1)
"""
