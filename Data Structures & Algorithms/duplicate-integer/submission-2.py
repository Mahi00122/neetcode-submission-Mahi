class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        for i in range(0, len(nums)):

            for j in range(i+1, len(nums)):

                if nums[j] == nums[i]:

                    return True
        return False
        