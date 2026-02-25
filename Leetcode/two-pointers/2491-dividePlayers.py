class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        totChem = 0
        left,right = 0, len(skill)-1
        target = skill[right]+skill[left]
        while left < right:
            if skill[right]+skill[left] != target:
                return -1
            totChem += skill[left]*skill[right]
            left+=1
            right-=1
        return totChem

        
