class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval : interval[0])
        res = [intervals[0]]

        for interval in intervals[1:]:
            lastEnd = res[-1][1]
            if interval[0] <= lastEnd:
                res[-1][1] = max(lastEnd, interval[1])
            else:
                res.append(interval)
        return res
