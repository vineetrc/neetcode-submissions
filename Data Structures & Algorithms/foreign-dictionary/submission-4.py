class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = defaultdict(list)
        indeg = defaultdict(int)


        for w in words:
            for c in w:
                indeg[c] = 0
                graph[c] = []

        for i in range(1,len(words)):
            first = words[i-1]
            second = words[i]

            if len(first) > len(second) and first.startswith(second):
                return ""
            for i in range(min(len(first), len(second))):
                if first[i] != second[i] :
                    if second[i] not in graph[first[i]]:
                        graph[first[i]].append(second[i])
                        indeg[second[i]]+=1
                    break
                        
    
        print(graph)
        print(indeg)
        q = deque()

        for val in graph:
            if indeg[val] == 0:
                q.append(val)

        res = []

        print(q)
        while q:
            
            v = q.popleft()
            res.append(v)

            for nxt in graph[v]:
                indeg[nxt] -=1
                if indeg[nxt] == 0:
                    q.append(nxt)
        

        print(res)
        if len(res) == len(graph):
            return "".join(res)

        return ""
