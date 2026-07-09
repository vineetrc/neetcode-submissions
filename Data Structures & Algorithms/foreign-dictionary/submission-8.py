class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for word in words:
            for c in word:
                graph[c] = []
                indeg[c] = 0

        for i in range(1,len(words)):
            first = words[i-1]
            second = words[i]

            if len(first) > len(second) and first.startswith(second):
                return ""

            for i in range(0, min(len(first), len(second))):
                if first[i] != second[i]:
                    if second[i] not in graph[first[i]]:
                        graph[first[i]].append(second[i])
                        indeg[second[i]]+=1
                    break

        print(graph)
        print(indeg)
        q = deque()
        for c , v in indeg.items():
            if v == 0:
                q.append(c)

        print(q)

        res = []
        while q:
            c = q.popleft()
            res.append(c)

            for nxt in graph[c]:
                indeg[nxt] -=1
                if indeg[nxt] ==0 :
                    q.append(nxt)

        if len(res) != len(indeg):
            return ""
        return "".join(res)
