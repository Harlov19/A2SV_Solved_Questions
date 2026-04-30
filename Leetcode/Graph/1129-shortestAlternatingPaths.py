class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redadj = defaultdict(list)
        blueadj = defaultdict(list)
        for a,b in redEdges:
            redadj[a].append(b)
        for u,v in blueEdges:
            blueadj[u].append(v)

        ans = [-1]*n
        ans[0] = 0

        q = deque([(0,'r'),(0,'b')])
        dis = 0
        
        visited = set([(0,'r'),(0,'b')])
        while q:
            for _ in range(len(q)):
                curr,lastColor = q.popleft()

                if lastColor == 'r':
                    for nei in blueadj[curr]:
                        if (nei,'b') in visited:continue
                        q.append((nei,'b'))
                        visited.add((nei,'b'))
                
                else: 
                    for nei in redadj[curr]:
                        if (nei,'r') in visited:continue
                        q.append((nei,'r'))
                        visited.add((nei,'r'))
                if ans[curr] == -1:
                    ans[curr] = dis
                    
            dis+=1

        return ans

