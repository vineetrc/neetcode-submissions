class Solution:
    def trap(self, height: List[int]) -> int:
        
        forpass = [0 for i in range(len(height)+2)]
        backpass = [0 for i in range(len(height)+2)]


        for i in range(len(height)):
            forpass[i + 1] = max(forpass[i], height[i])

        for i in range(len(height)-1, -1, -1):
            backpass[i + 1] = max(backpass[i+2], height[i])

        print(forpass)
        print(backpass)
        tot = 0
        for i in range(0,len(height)):
            tot += max(0, min(forpass[i+1], backpass[i+1]) - height[i])
            print(tot)
        return tot