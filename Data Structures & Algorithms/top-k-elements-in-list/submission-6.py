class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        buckets = [[] for _ in range(n + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)
        res = []
        size = 0
        for i in range(n, 0, -1):
            for num in buckets[i]:
                if size < k:
                    res.append(num)
                    size += 1
                else:
                    return res
        return res
                



