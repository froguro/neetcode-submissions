class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # this stores the counts of each value in nums
        freqs = [[] for i in range(len(nums) + 1)]

        # first iteration
        for num in nums:
            count[num] += 1
        # second iteration
        for num, cnt in count.items():
            freqs[cnt] += [num]
        
        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                res += [num]
                if len(res) == k:
                    return res
            

