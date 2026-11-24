"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return 1
        
        intervals.sort(key = lambda interval: (interval.start, interval.end))
        res = 0
        lastEnd = intervals[0].end

        heap = []
        for interval in intervals[1:]:
            if interval.start < lastEnd:
                heapq.heappush(heap, interval.end)
            else:
                heapq.heappop(heap)
        return len(heap)





