class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # count frequency
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        sorted_f = sorted(freq, key = freq.get, reverse = True)
        return sorted_f[:k]