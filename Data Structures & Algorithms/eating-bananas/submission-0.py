class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')

        for i in range(1, max(piles) + 1):
            curr = 0
            for pile in piles:
                curr += math.ceil(pile / i)
            
            if curr <= h:
                res = min(res, i)
        return res
