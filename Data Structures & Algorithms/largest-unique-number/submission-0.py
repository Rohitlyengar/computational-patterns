class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        countN = {}
        res = float('-inf')

        for num in nums:
            countN[num] = 1 + countN.get(num, 0)
        
        for key, val in countN.items():
            res = max(res, key if val == 1 else res)
        return res if res != float('-inf') else -1
