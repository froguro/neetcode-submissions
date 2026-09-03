class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # character -> last idx seen
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
            
        
        return res
            

