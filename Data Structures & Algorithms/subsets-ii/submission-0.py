class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort()

        out = []
        def dfs(idx, res):
            if idx == len(nums):
                out.append(res.copy())
                return
            
            # take
            res.append(nums[idx])
            dfs(idx + 1, res)
            res.pop()
            
            # do not take, dont take same 

            while idx + 1 < len(nums) and nums[idx+1] == nums[idx]:
                idx +=1

            dfs(idx+1, res)

        dfs(0,[])

        return out