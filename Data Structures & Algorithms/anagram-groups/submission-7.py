class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """DefaultDict, 
        two strings are an anagram of each other if they have the same letter frequency
        """
        def findFreq(s):
            freqs = [0] * 26 # this can be an array 
            for c in s:
                freqs[ord(c) - ord('a')] += 1
            return tuple(freqs)

        # new idea: hash table that maps freq to array of strings
        freqMap = defaultdict(list)
        for s in strs:
            freq = findFreq(s)
            freqMap[freq].append(s)
        
        return list(freqMap.values())