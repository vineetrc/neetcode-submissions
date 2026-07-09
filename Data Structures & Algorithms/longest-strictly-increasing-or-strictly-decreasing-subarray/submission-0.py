class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        max_len = 0
        l = 1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                l+=1
            else:
                max_len = max(max_len, l)
                l = 1

        max_len = max(max_len, l)
        
        max_len_b = 0
        l = 1
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                l+=1
            else:
                max_len_b = max(max_len_b, l)
                l = 1
        max_len_b = max(max_len_b, l)

        # print(max_len_b)
        return max(max_len_b, max_len)