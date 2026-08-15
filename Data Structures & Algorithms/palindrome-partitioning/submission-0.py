class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtracking(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(i, j, s):
                    part.append(s[i:j + 1])
                    backtracking(j + 1)
                    part.pop()
        backtracking(0)
        return res

    def isPalindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True