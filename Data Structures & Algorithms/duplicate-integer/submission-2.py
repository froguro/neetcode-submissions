class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqs = defaultdict(int)
        for num in nums:
            if freqs[num] > 0:
                return True
            freqs[num] += 1
        return False