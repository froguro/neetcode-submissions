class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = {}
        for num in nums:
            unique_nums[num] = 1 + unique_nums.get(num,0)
        
        sorted_nums = dict(sorted(unique_nums.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_nums)[:k]
