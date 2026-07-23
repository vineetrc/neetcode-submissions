class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort(key = lambda x: (x[0],x[1]))

        res = []
        hold = intervals[0][0]
        until = intervals[0][1]

        for i in range(1,len(intervals)):
            s,e = intervals[i]

            if (s >= hold and s <= until) or (e >= hold and e <= until) :
                until = max(until, e)
            else:
                res.append([hold,until])
                hold = s
                until = e
        

        res.append([hold,until])

        return res
