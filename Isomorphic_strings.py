class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        indexS = [0] * 200 # Stores index of characters in string s
        indexT = [0] * 200 # Stores index of characters in string t
        
        length = len(s) # Get the length of both strings
        
        if length != len(t): # If the lengths of the two strings are different, they can't be isomorphic
            return False
            
        for i in range(length):
            print(indexS[ord(s[i])])
            print(indexT[ord(t[i])])
            if indexS[ord(s[i])] != indexT[ord(t[i])]:
                return False

            indexS[ord(s[i])] = i + 1
            indexT[ord(t[i])] = i + 1
        
        return True
                
test = Solution()
print(test.isIsomorphic("bbbaaaba", "aaabbbba"))