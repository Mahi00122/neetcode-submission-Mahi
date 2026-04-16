class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[j] + nums[i] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                
                        if triplet not in result:

                            result.append(triplet)
        return result
                    