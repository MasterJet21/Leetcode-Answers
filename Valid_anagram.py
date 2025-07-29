class Solution:
    def isAnagram(self, s, t):
        d = {}
        for i in s:
            if i not in d:
                d.update({i: 1})
            else:
                d[i] = d.get(i) + 1

        for j in t:
            if j in d:
                d[j] = d.get(j) - 1
            else:
                return False

        for k in s:
            if d[k] != 0:
                return False
        
        print(d)
        return True

test = Solution()
test.isAnagram("anagram", "nagaram")