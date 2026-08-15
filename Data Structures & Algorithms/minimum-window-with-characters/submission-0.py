class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tCount, sCount = {}, {}
        for i in t:
            tCount[i] = tCount.get(i, 0) + 1

        have, need = 0, len(tCount)
        l = 0

        res, reslen = "", float('inf')
        for r in range(len(s)):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1
                while have == need:
                    if r - l + 1 < reslen:
                        res = s[l: r + 1]
                        reslen = r - l + 1
                    
                    sCount[s[l]] -= 1

                    if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                        have -= 1
                    l += 1
        
        return res

