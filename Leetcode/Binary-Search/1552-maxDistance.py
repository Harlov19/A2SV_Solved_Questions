class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(d):
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= d:
                    count += 1
                    last = position[i]
                    if count == m:
                        return True
            return False

        l = 1
        r = position[-1] - position[0]
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            if can_place(mid):
                ans = mid
                l = mid + 1   
            else:
                r = mid - 1  

        return ans
