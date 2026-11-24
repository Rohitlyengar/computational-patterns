class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = 0

        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            curMin, curMax = min(num, num * curMin, num * curMax), max(num, num * curMin, num * curMax)
            res = max(res, curMax)
        return res
