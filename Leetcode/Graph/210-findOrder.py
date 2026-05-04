class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)

        visited = set()
        inStack = set()

        order = []
        def dfs(node):
            if node in inStack:
                return True
            if node in visited:
                return False
            visited.add(node)
            inStack.add(node)

            for nei in graph[node]:
                if dfs(nei):
                    return True
            order.append(node)
            inStack.remove(node)
            return False
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return []
       
        return order[::-1]
