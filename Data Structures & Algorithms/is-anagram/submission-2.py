class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for i in range(len(s)):
            freq1[s[i]] += 1
            freq2[t[i]] += 1
        
        return freq1 == freq2

