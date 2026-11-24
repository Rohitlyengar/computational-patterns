class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < target:
                    res += 1
                    r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
            
        return res
