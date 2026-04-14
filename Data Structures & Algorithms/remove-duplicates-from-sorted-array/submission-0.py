class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0 # unique elements 
        for j in range(1, len(nums)):
            if nums[j] != nums[k]:

                k += 1
                nums[k] = nums[j]
                
        return k + 1
        

        