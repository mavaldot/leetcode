class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        prev = intervals[0]
        remove = 0
        for interval in intervals[1:]:
            if interval[0] < prev[1]:
                remove += 1
                if interval[1] < prev[1]:
                    prev = interval
            else:
                prev = interval
        return remove