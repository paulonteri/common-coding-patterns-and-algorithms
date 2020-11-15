"""
Merge Intervals:

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
Example:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
    one [1,5].
"""
from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


# space O(n)
# time O(N ∗ logN) -> because of (iteration * sort)
def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    merged = []
    # add first item -> will be first prev
    merged.append(intervals[0])
    for curr in intervals:
        prev = (merged[-1])  # last one added

        # overlapping can be narrowed down to two major conditions:
        # the curr.start can either be before the prev.start or prev.end
        if curr.start < prev.start:
            # # MERGE
            # temp = Interval(curr.start, max(prev.end, curr.end))
            # merged[-1] = temp
            prev.start = curr.start
            prev.end = max(prev.end, curr.end)
        elif curr.start < prev.end:
            # # MERGE
            # temp = Interval(prev.start, max(prev.end, curr.end))
            # merged[-1] = temp
            prev.end = max(prev.end, curr.end)
        else:
            merged.append(curr)

    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
