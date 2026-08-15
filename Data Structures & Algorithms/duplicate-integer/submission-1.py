class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        joe = set()
        for i in nums:
            if i in joe: return True
            joe.add(i)
        return False