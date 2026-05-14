class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        tot = 0

        b = 0
        e = len(heights)-1

        while b < e:
            
            tot = max(tot, (e - b) * min(heights[b],heights[e]))
            if heights[b] < heights[e]:
                b+=1
            else:
                e-=1
        
        return tot

    