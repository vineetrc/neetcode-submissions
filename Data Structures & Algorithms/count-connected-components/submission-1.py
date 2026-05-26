class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        graph = {i : [] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        vset = set()

        def dfs(n,p):

            if n in vset:
                return False
            
            vset.add(n)
            for nx in graph[n]:
                if nx == p:
                    continue
                dfs(nx,n)        
        
        cnt = 0
        for i in range(n):
            if i not in vset:
                dfs(i,-1)
                cnt +=1
        
        return cnt
            
            
