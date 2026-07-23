class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        intervals.sort(key = lambda x: (x[1], x[0]))

        until = -float('inf')
        cnt = 0
        for i in range(len(intervals)):
            s,e = intervals[i]
            
            if s < until:
                cnt +=1
            else:
                until = e
        
        return cnt



            




        return 0

