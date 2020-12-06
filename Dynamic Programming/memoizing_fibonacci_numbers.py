"""
Memoizing Fibonacci Numbers:

The memoized version of a problem is similar to the regular recursive version;
 the difference is that it looks for the answer of a subproblem in a lookup table before computing its solution.
If the precomputed value exists, then it is returned. 
Otherwise, the value is computed and put in the lookup table so that it can be reused later.

"""


def getFibHelper(num, store):
    if num in store:
        # check if the value is already present in the store and return it
        return store[num]

    else:
        # when we find a solution we save it to the store before returning it
        sol = getFibHelper(num-1, store) + getFibHelper(num-2, store)
        store[num] = sol
        return sol


def getFib(num):

    store = {
        0: 0,
        1: 1
    }

    return getFibHelper(num, store)


print(getFib(15))
print(getFib(10))
print(getFib(6))
