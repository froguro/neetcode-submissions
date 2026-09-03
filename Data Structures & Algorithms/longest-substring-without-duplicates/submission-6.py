class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # character -> last idx seen
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
            
        
        return res
            

