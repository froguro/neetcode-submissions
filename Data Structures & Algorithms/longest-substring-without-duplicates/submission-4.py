class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # stores the last time s[r] was seen
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l) # removes the last occurrence of s[r] from the window
            mp[s[r]] = r # now the last occurrence of s[r] is at r
            res = max(res, r - l + 1)
        return res
