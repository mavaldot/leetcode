class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if ((prev[1] >= intervals[i][0] and prev[1] <= intervals[i][1]) 
            or (prev[0] >= intervals[i][0] and prev[0] <= intervals[i][0])
            or (intervals[i][0] >= prev[0] and intervals[i][0] <= prev[0]) 
            or (intervals[i][1] >= prev[0] and intervals[i][1] <= prev[1])):
                prev = [min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1])]
            else:
                res.append(prev)
                prev= intervals[i]

        res.append(prev)
        return res