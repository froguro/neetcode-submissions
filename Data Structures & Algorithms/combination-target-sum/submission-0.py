class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        def backtracking(i, currSum, currSet):
            if i >= len(nums):
                return
            if currSum > target:
                return
            if currSum == target:
                res.add(tuple(currSet.copy()))
                return
            
            currSet.append(nums[i])
            backtracking(i, currSum + nums[i], currSet)
            backtracking(i + 1, currSum + nums[i], currSet)

            currSet.pop()
            backtracking(i + 1, currSum, currSet)
        backtracking(0, 0, [])
        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res


                

        