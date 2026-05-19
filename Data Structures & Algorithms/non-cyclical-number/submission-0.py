class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper_sum(x):
            res = 0
            while x > 0 :
                res += ((x%10) * (x%10))
                x = x // 10

            return res
        
        visit = set()
        val = helper_sum(n)
        while True:
            if val == 1:
                return True
            if val in visit:
                return False
            else:
                visit.add(val)
                val = helper_sum(val)

        return True