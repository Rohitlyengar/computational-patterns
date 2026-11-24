class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] + nums[r] == target:
                return [nums[l], nums[r]]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return res
