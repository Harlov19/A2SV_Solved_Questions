class Solution:
    def numRabbits(self, answers: List[int]) -> int:
       counts = Counter(answers) 
       ans = 0
       for key,value in counts.items():
            group = math.ceil(value/(key+1))
            ans += group*(key + 1)
       return ans
