class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for path in paths:
            path = path.split(" ")
            root = path[0]
            for i in range(1,len(path)):
                file = path[i]
                left = file.find('(')
                right = file.find(")")
                directory = f"{root}/{file[:left]}"
                content = file[left+1:right]
                counts[ content].append(directory)
           
        return [group for group in counts.values() if len(group)>1]
