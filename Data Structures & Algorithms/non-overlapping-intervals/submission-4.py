class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval : interval[0])
        res = 0
        lastEnd = intervals[0][1]

        for interval in intervals[1:]:
            if lastEnd > interval[0]:
                res += 1
                lastEnd = min(lastEnd, interval[1])
            else:
                lastEnd = interval[1]
        return res
