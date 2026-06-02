class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        
        q = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        

        visit = set()
        while q:
            r,c,h = q.popleft()

            if r < 0 or c < 0 or  r >= len(grid) or c >= len(grid[0]) or grid[r][c] == -1:
                continue
            


            if grid[r][c] > 0 and grid[r][c] != 2147483647 :
                continue

            else:
                if grid[r][c] != 0:
                    grid[r][c] = h
                q.append((r+1,c,h+1))
                q.append((r-1,c,h+1))
                q.append((r,c+1,h+1))
                q.append((r,c-1,h+1))
        

               

            
            




