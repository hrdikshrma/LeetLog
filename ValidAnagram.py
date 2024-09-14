#Question: Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Solution 1: Using the built-in functions
        return sorted(s) == sorted(t)
    
        #Solution 2: Using hashmap
        #Time complexity: O(S+T)
        #Space complexity: O(S+T)
        if len(s) == len(t):
            return False
        
        countS, countT = {},{}
        for i in len(s):
            countS[s[i]] = 1 + countS.get(s[i], 0) #Used get() in case the key already doesn't exist
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True
                