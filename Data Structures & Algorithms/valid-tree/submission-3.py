class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        graph = {i : [] for i in range(n)}


        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        vset = set()
        def dfs(n, p):
            if n in vset:
                return False
            
            vset.add(n)
            for nx in graph[n]:
                if nx == p:
                    continue
                if not dfs(nx,n): return False
            
            return True

        return dfs(0, -1) and len(vset) == n
        
