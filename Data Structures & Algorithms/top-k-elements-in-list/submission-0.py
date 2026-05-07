class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = [[] for i in range(0, len(nums) +1)]

        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        for x,v in freq.items():
            heap[v].append(x)
        
        i = len(nums)

        print(heap)
        out = []
        while i >= 0 and len(out) < k:
            print(len(out))
            out+=heap[i]
            i-=1

        return out