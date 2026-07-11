class Solution:
    def maxSubArray(self, nums):
        current = nums[0]
        maximum = nums[0]
        for i in nums[1:]:
            current = max(i, current+i)
            maximum = max(maximum, current)
        return maximum
       