"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key = lambda x: (x.start, x.end))
        heap = []
        res = 0
        for inter in intervals:
            start = inter.start
            end = inter.end
            while len(heap) > 0 and heap[0][0] <=start:
                heapq.heappop(heap)
            
            res = max(res, len(heap)+1)
            heapq.heappush(heap,(end,start))
        
        return res


            



        