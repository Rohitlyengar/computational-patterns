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
            return len(intervals)
        
        heap = [intervals[0].end]
        intervals.sort(key = lambda interval : interval.start)

        for interval in intervals[1:]:
            if interval.start < heap[0]:
                heapq.heappush(heap, interval.end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
        return len(heap)
