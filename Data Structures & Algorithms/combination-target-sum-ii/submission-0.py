class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()


        def backtracking(i, currSum, currSet):
            if currSum == target:
                res.append(currSet.copy())
                return
            if i >= len(candidates) or currSum > target:
                return

            
            
            
            currSet.append(candidates[i])
            backtracking(i + 1, currSum + candidates[i], currSet)
            currSet.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtracking(i + 1, currSum, currSet)
        
        backtracking(0, 0, [])
        return res