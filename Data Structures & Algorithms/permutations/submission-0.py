class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(seen, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
            
            for i in range(len(nums)):
                if not seen[i]:
                    curr.append(nums[i])
                    seen[i] = True
                    backtracking(seen, curr)
                    curr.pop()
                    seen[i] = False

        backtracking([False] * len(nums), [])
        return res
