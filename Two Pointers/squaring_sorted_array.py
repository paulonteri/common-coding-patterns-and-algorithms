"""
Squaring a Sorted Array
Given a sorted array, 
 create a new array containing squares of all the number of the input array in the sorted order.
"""


# Remember that the array is sorted! :)
def make_squares(arr):
    squares = []

    # note that the largest squares will be at the furthest ends 0 & (len(arr)-1)
    left, right = 0, (len(arr)-1)
    while left <= right:
        right_square = arr[right]**2
        left_square = arr[left]**2

        # if left_square is greater than the right_square,
        # add the left_square first
        if left_square >= right_square:
            # inserting the largest values at a given time,
            #  at index 0 will ensure a sorted order i.e [0,2,4,6,7]
            #  because smaller values will be added later on
            squares.insert(0, left_square)
            left += 1

        elif left_square < right_square:
            squares.insert(0, right_square)
            right -= 1
    return squares


def make_squares_two(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highestSquareIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1

    return squares


def main():
    print("Squares: " + str(make_squares([-2, -1, 0,  2, 3])))
    print("Squares: " + str(make_squares_two([-2, -1, 0,  2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))
    print("Squares: " + str(make_squares_two([-3, -1, 0, 1, 2])))


main()

"""
SOLUTION: make_squares_two:
This is a straightforward question. 
The only trick is that we can have negative numbers in the input array, 
which will make it a bit difficult to generate the output array with squares in sorted order.

Since the numbers at both the ends can give us the largest square,
 we can use two pointers starting at both the ends of the input array.
At any step, whichever pointer gives us the bigger square we add it to the result array and
 move to the next/previous number according to the pointer. 
"""
