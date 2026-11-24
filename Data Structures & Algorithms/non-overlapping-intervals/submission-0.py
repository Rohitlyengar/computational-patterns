class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval : interval[0])
        lastEnd = intervals[0][1]
        res = -1

        for start, end in intervals[1:]:
            if start > lastEnd:
                lastEnd = end
            else:
                res += 1
                lastEnd = max(end, lastEnd)
        return res
