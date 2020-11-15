"""
Insert Interval:

Given a list of non-overlapping intervals sorted by their start time,
 insert a given interval at the correct position and merge all necessary intervals
  to produce a list that has only mutually exclusive intervals.

Example:
    Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
    Output: [[1,4], [5,7]]
    Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""
# Note: The array is sorted :)


# O(N) time | O(N) space
def insert(intervals, new_interval):
    merged = []

    idx = 0
    # skip (and add to output) all intervals that come before the 'new_interval'
    while idx < len(intervals) and intervals[idx][1] < new_interval[0]:
        merged.append(intervals[idx])
        idx += 1

    # # figure out the starting and ending interval
    if idx < len(intervals):
        start = min(intervals[idx][0], new_interval[0])
        end = max(intervals[idx][1], new_interval[1])
    else:
        # edge case where we will insert at the very end
        start = new_interval[0]
        end = new_interval[1]

    # merge all intervals that overlap with 'new_interval'
    while idx < len(intervals) and intervals[idx][0] < new_interval[1]:
        end = max(intervals[idx][1], new_interval[1])
        idx += 1
     # insert the new_interval
    merged.append([start, end])

    # add all the remaining intervals to the output
    while idx < len(intervals):
        merged.append(intervals[idx])
        idx += 1

    return merged


def main():
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " +
          str(insert([[2, 3], [5, 7]], [1, 4])))
    print("Intervals after inserting the new interval: " +
          str(insert([[2, 3], [5, 7]], [8, 9])))


main()
