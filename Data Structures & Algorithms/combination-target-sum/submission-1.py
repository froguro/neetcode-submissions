class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(i, currSum, currSet):
            if i >= len(nums):
                return
            if currSum > target:
                return
            if currSum == target:
                res.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            backtracking(i, currSum + nums[i], currSet)

            currSet.pop()
            backtracking(i + 1, currSum, currSet)
        backtracking(0, 0, [])
        return res


                

        