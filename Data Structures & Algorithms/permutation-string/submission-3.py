class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        a valid window in s2 contains all of the elements in s1
        """
        
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1    
            s2Count[ord(s2[i]) - ord('a')] += 1    
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # check the right pointer (just incremented)
            idx = ord(s2[r]) - ord('a')
            s2Count[idx] += 1
            if s2Count[idx] == s1Count[idx]:
                matches +=1
            elif s2Count[idx] == s1Count[idx] + 1: # if it became a mismatch after the update (too many)
                matches -= 1

            # check the left pointer (about to get rid of a character from the window)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1 # because we will increment left soon

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]: # if it became a mismatch after
                matches -= 1
            
            l += 1

        return matches == 26
            
                
            
