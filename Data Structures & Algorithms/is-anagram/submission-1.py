class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        count2= [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in t:
            count2[ord(i) - ord('a')] += 1
        if count == count2: return True
        else: return False
