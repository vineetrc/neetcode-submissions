class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = {i: [] for i in range(numCourses)}
        indegree = [0 for i in range(numCourses)]


        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] +=1
        
        print(graph, indegree)

        q = deque()
        completed = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        

        while q:
            crs = q.popleft()

            completed +=1
            for i in graph[crs]:
                indegree[i] -=1
                if indegree[i] == 0:
                    q.append(i)
        

        return completed == numCourses
