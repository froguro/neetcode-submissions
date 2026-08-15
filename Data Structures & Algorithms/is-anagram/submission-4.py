class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs1 = [0] * 26
        freqs2 = [0] * 26
        for c in s:
            freqs1[ord(c) - ord('a')] += 1
        for c in t:
            freqs2[ord(c) - ord('a')] += 1
        

        return freqs1 == freqs2
