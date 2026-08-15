class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqmap = defaultdict(list)
        for word in strs:
            # make a freq map for the word, store it in its own map?
            temp = [0] * 26
            for i in range(len(word)):
                temp[ord(word[i]) - ord('a')] += 1
            freqmap[tuple(temp)].append(word)
        
        return list(freqmap.values())