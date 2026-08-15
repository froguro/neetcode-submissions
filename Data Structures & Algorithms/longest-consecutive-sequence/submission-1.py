class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            naive approach: sort then linearly count (O(nlogn))
            better way: 
                - store values in some data structure
                - get the length ???
                - two linear passes -> O(n) 
                - determining the start of a sequence: if a number n is the start, then n-1 doesn't exist but n+1 does
        """
        if len(nums) == 0:
            return 0
        n_set = set(nums)
        max_length = 1
        for n in n_set:
            if (n - 1) not in n_set and (n + 1) in n_set:
                i = n + 1
                curr_length = 2
                while True:
                    if (i + 1) in n_set:
                       curr_length += 1 
                       i += 1
                    else: 
                        break
                max_length = max(max_length, curr_length)
        return max_length

