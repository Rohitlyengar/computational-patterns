class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if i > 0 and nums[i] % 2 == nums[i - 1] % 2:
                return False
        return True
