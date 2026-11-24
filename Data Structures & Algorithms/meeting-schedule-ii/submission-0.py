"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 1
        intervals.sort(key = lambda interval: (interval.start, interval.end))
        lastEnd = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < lastEnd:
                res += 1
                lastEnd = min(lastEnd, interval.end)
        return res

