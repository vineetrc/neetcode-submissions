class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        


        res = []
        ns,ne = newInterval

        i = 0
        n = len(intervals)

        while i < n:
            s,e = intervals[i]
            
            if e < ns:
                res.append(intervals[i])
                i+=1
            else:
                break
        
        hold = ns
        until = ne
        while i < n:
            s,e = intervals[i]
            if s <= ne or e <= ne:
                hold = min(hold, s)
                until = max(until,e)
                i+=1
            else:
                break
        
        res.append([hold,until])

        while i < n:
            res.append(intervals[i])
            i+=1
        

        return res





