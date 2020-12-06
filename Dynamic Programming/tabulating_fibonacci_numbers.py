"""
Tabulating Fibonacci Numbers:

Tabulation is the opposite of the top-down approach and avoids recursion. 
In this approach, we solve the problem “bottom-up” (i.e. by solving all the related subproblems first).
This is typically done by filling up a lookup table and based on the results in the table, the solution to the top/original problem is then computed.

"""


def getFib(num, lookup_table={}):
    # Set 0th and 1st values
    lookup_table[0] = 0
    lookup_table[1] = 1

    for i in range(2, num + 1):
        # Fill up the table by summing up previous two values
        lookup_table[i] = lookup_table[i - 1] + lookup_table[i - 2]

    return lookup_table[num]  # Return the nth Fibonacci number


"""

If you look at the previous code closely, 
 you’ll notice that only the preceding two Fibonacci numbers are required at any given iteration of the for loop to calculate the next one.
So, we don’t need to save all of the previous ones except for the last two.
We can get rid of the lookup table and only save the last two numbers in variables,
 reducing the space complexity as done in the following Python implementation.

"""


def getFib2(num):
    # Base Case
    if num == 0:
        return 0

    second_last = 0  # The 0th
    last = 1  # The first
    current = 0

    for _ in range(2, num + 1):
        # current is the sum of the last plus second last number before the current one
        current = second_last + last
        second_last = last
        last = current

    return current


print(getFib2(15))
print(getFib(15))

print(getFib2(10))
print(getFib(10))

print(getFib2(6))
print(getFib(6))
