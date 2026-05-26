class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # count frequency
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        # sort by frequency
        sorted_freq = sorted(freq, key=freq.get, reverse=True)

        # return top k elements
        return sorted_freq[:k]
        