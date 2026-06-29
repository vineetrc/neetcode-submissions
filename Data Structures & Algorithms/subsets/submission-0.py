class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        out = []

        def dfs(idx, res):

            if idx == len(nums):
                out.append(res.copy())
                return
            
            res.append(nums[idx])
            dfs(idx+1, res)
            res.pop()

            dfs(idx+1, res)


        dfs(0,[])

        return out
            