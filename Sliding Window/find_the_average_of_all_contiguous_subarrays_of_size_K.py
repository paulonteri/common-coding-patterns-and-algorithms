"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
"""


def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0, 0

    for windowEnd in range(len(arr)):
        # add the next element to window
        windowSum += arr[windowEnd]

        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K)  # calculate the average
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead

    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
