class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""


        sCount, tCount = {}, {}

        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        l = 0
        res = ""
        resLen = float('inf')
        have, need = 0, len(tCount)
        for r in range(len(s)):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1
            if have == need:
                while have == need:
                    if r - l + 1 < resLen:
                        resLen = r - l + 1
                        res = s[l: r + 1]
                    sCount[s[l]] -= 1
                    if s[l] in tCount and sCount[s[l]] == tCount[s[l]] - 1:
                        have -= 1
                    l += 1

        return res
