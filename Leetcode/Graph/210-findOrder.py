class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        
        while q:
            curr = q.popleft()
            order.append(curr)
            for nei in graph[curr]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(order) != numCourses:
            return []
       
        return order
