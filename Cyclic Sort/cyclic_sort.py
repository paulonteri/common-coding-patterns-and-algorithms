"""
Cyclic Sort:
We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. 
 This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space.
 For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.
"""
# Note: sort the objects in-place, the numbers are from 1-n


# O(n) time | O(1) space
def cyclic_sort(nums):
    idx = 0
    while idx < len(nums):
        num = nums[idx]
        if num == idx + 1:
            idx += 1
        else:
            # # swap
            # place num in the correct index (num-1)
            temp_num = nums[num-1]
            nums[num-1] = num
            # move the number that was at the correct index(num-1) to the current index(idx)
            nums[idx] = temp_num
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()

"""
SOLUTION:
As we know, the input array contains numbers in the range of 1 to ‘n’. We can use this fact to devise an efficient way to sort the numbers.
 Since all numbers are unique, we can try placing each number at its correct place, i.e., placing ‘1’ at index ‘0’, placing ‘2’ at index ‘1’, and so on.

To place a number (or an object in general) at its correct index, we first need to find that number. 
If we first find a number and then place it at its correct place, it will take us O(N^2)O(N​2), which is not acceptable.

Instead, what if we iterate the array one number at a time, and if the current number we are iterating is not at the correct index,
 we swap it with the number at its correct index. This way we will go through all numbers and place them in their correct indices,
  hence, sorting the whole array.
"""
