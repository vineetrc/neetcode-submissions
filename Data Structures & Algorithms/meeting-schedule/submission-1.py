"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i : i.start)

        for i in range(1,len(intervals)):
            s = intervals[i-1]
            ss = intervals[i]
            if ss.start >= s.start and ss.start < s.end:
                return False
            if ss.end >= s.start and ss.end < s.end:
                return False
        
        return True

