class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        return the length of the longest substring
        """

        l, r = 0, 0
        # maintain valid substring
        length = 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            length = max(length, r - l + 1)
            seen.add(s[r])
            r += 1


        return length


