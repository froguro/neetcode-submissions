class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current):
            res.append(list(current))
            for i in range(start, len(nums)):
                # skip duplicates
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                backtrack(i + 1, current)

                current.pop()
            

        res = []
        nums.sort()
        backtrack(0, [])
        return res