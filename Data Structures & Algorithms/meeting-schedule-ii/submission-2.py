class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda interval: (interval.start, interval.end))
        rooms = [intervals[0].end]

        for interval in intervals[1:]:
            if interval.start < min(rooms):
                rooms.append(interval.end)
            else:
                rooms.remove(min(rooms))
                rooms.append(interval.end)
        
        return len(rooms)