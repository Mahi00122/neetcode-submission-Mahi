class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #res is best pos for target
        res = len(nums)
        l = 0
        r = res -1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                res = mid
                r = mid - 1 #right ko squeez kro 
            else:
                l = mid + 1 # left ko squeez  kro 
        return res
        