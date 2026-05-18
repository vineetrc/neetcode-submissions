from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        def help_add(i,j,v,q):
            if min(i,j) < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return
            if grid[i][j] == 2:
                return
            if grid[i][j] == 1:
                q.add((i,j,v))

        q = deque()
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j] == 1:
                    cnt +=1
        
        visit = set()
        time = 0
        while q:
            print(q)
            i,j,v = q.popleft()
            
            if min(i,j) < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                continue

            if (i,j) in visit:
                continue

            visit.add((i,j))
            
            if grid[i][j] == 1:
                q.append((i+1,j,v+1))
                q.append((i-1,j,v+1))
                q.append((i,j+1,v+1))
                q.append((i,j-1,v+1))
                cnt -=1
                time = max(time,v)
            
            if grid[i][j] == 2:
                q.append((i+1,j,v+1))
                q.append((i-1,j,v+1))
                q.append((i,j+1,v+1))
                q.append((i,j-1,v+1))
                time = max(time,v)


        if cnt == 0:
            return time
        return -1