class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        i = 0
        ans = []
        in_block = False
        curr = ""
        for line in source:
            i = 0
            while(i<len(line)):
                 if(line[i:i+2] == "//" and   not in_block):
                     break
                 elif(line[i:i+2] == "/*" and  not in_block):
                     i+=2
                     in_block = True
                 elif(line[i:i+2] == "*/" and  in_block):
                     in_block = False
                     i+=2
            
                 else:
                      if(not in_block):
                          curr+=line[i]
                      i+=1
            if(curr and not in_block):
                ans.append(curr)
                curr = ""

        return ans

