class Solution:
    def maxSubArray(self, nums) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)