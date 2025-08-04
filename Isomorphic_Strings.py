class Solution:
    def isIsomorphic(self, s, t):
        d = {}
        for i in range(len(s)):
            if s[i] not in d and s[i] != d[s[i]]:
                d.update({s[i]: t[i]})
                print(d[s[i]])
                print(s[i])
            else:
                return False
            print(d[s[i]])
            print(s[i])
        print(d)
    
test = Solution()
test.isIsomorphic("egg", "add")