"""
Merge Overlapping Intervals

Write a function that takes in an non-empty array of arbitrary intervals,
merges any overlapping intervals, and returns the new intervals in no 
particular order.

Each interval is an array of two intergers, with interval[0] as the start
of the interval and interval[1] as the end of the interval.

Note that back-to-back intervals aren't considered to be overlapping. For
example [1, 5] and [6, 7] aren't overlapping; however [1, 6] and [6, 7] are
overlapping.

Also note that the start of any particular interval will always be less than
or equal to the end of that interval.
"""

"""
[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
                                           ^
current: [9, 10]
ans: [[1, 2], [3, 8], [9, 10]]


"""
def merge(r1, r2):
    return [min(r1[0], r2[0]), max(r1[1], r2[1])]
def overlapping(r1, r2):
    if (r2[0] <= r1[1]) and (r2[1] >= r1[0]):
        return True
    return False
def mergeOverlappingIntervals(intervals):
    intervals.sort()
    ans = []
    i = 0
    while i < len(intervals):
        current = intervals[i]
        while i < len(intervals) and overlapping(intervals[i], current):
            current = merge(current, intervals[i])
            i += 1
        ans.append(current)
    return ans
