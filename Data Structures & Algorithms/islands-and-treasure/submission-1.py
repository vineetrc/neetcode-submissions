from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
            def bfs(i,j):
                q = deque()
                visit = set()
                q.append((i+1,j, 1))
                q.append((i-1,j, 1))
                q.append((i,j+1, 1))
                q.append((i,j-1, 1))

                while len(q) > 0:
                    x,y,v = q.popleft()

                    if x < 0 or y < 0 or x >=len(grid) or y >= len(grid[0]):
                        continue
                    if grid[x][y] == -1 or grid[x][y] == 0 or (x,y) in visit:
                        continue
                    else:
                        grid[x][y] = min(grid[x][y],v)
                        visit.add((x,y))
                        q.append((x+1,y, v+1))
                        q.append((x-1,y, v+1))
                        q.append((x,y+1, v+1))
                        q.append((x,y-1, v+1))

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        bfs(i,j) 
                






