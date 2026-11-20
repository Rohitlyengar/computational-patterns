class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = max(nums)

        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            curMax, curMin = max(num, curMax * num, curMin * num), min(num, curMax * num, curMin * num)
            res = max(res, curMax)
        return res
