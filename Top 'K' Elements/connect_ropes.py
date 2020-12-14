"""
Connect Ropes:

Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost.
The cost of connecting two ropes is equal to the sum of their lengths.

Example:
    Input: [1, 3, 11, 5, 2]
    Output: 42
    Explanation: 
        First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22). Total cost is 42 (3+6+11+22)
"""
import heapq


def minimum_cost_to_connect_ropes(ropeLengths):

    heapq.heapify(ropeLengths)

    cost_of_connects = 0
    i = len(ropeLengths)
    while i > 1:
        one = heapq.heappop(ropeLengths)
        two = heapq.heappop(ropeLengths)
        total = one + two

        cost_of_connects += total
        heapq.heappush(ropeLengths, total)

        i -= 1

    return cost_of_connects


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()

"""
Solution:

In this problem, following a greedy approach to connect the smallest ropes first will ensure the lowest cost.
We can use a Min Heap to find the smallest ropes following a similar approach as discussed in Kth Smallest Number.
Once we connect two ropes, we need to insert the resultant rope back in the Min Heap so that we can connect it with the remaining ropes.
"""
