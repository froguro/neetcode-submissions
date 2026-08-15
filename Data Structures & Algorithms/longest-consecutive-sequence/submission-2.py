class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        [2,20,4,10,3,4,5]
        [0,3,2,5,4,6,1,1]
        find starting points:
        - numbers that don't have anything directly less than it (num[i] - 1 DNE)
        '''

        unique = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in unique:
                curr = 1
                while num + 1 in unique:
                    num = num + 1
                    curr += 1
                res = max(curr, res)
        
        return res
                



        
