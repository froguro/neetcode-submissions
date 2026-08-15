class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs1 = {}
        freqs2 = {}
        for c in s:
            freqs1[c] = freqs1.get(c, 0) + 1
        for c in t:
            freqs2[c] = freqs2.get(c, 0) + 1
        

        return freqs1 == freqs2
