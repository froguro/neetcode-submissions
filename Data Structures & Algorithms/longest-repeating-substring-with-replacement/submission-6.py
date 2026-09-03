class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freqs = {}
        l, r = 0, 0
        currMax = 0

        while r < len(s):
            windowLength = r - l + 1
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            currMax = max(currMax, freqs[s[r]])
            if windowLength - currMax <= k:
                res = max(res, windowLength)
            else:
                freqs[s[l]] -= 1
                l += 1
            r += 1

        





        return res