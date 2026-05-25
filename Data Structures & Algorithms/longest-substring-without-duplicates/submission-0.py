class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #variable size window 
        # two pointer needed 
        # its not about comparing i and j but duplicate element 
        subset = set() # these will store all elements and remove duplicate one 
        left = 0
        length = 0
        for r in range (len(s)):
            while s[r] in subset:
                subset.remove(s[left])
                left += 1
            subset.add(s[r])
            length = max(length, r-left+1)
        return length  