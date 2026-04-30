class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set([0])
    
        while q:
            curr = q.popleft()
            for nei in rooms[curr]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
            
        return len(visited)== len(rooms)
        
