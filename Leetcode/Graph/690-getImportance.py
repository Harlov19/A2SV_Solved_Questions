"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        priority = {}
        for emp in employees:
            graph[emp.id].extend(emp.subordinates)
            priority[emp.id] = emp.importance

        visited = set()
        def dfs(id):
            if id in visited:
                return 0
            visited.add(id)
            
            res = priority[id]
            for nei in graph[id]:
                res += dfs(nei)
            return res
        return dfs(id)
