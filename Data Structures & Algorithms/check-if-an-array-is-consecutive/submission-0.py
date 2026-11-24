class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return False
        
        count = 0
        next = min(nums)

        while next in nums:
            next = next + 1
            count += 1
        
        return count == len(nums)
