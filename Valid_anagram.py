class Solution:
    def isAnagram(self, s, t):
        d ={}
        for i in s:
            if i not in d:
                d.update({i: 1})
            else:
                d[i] = d.get(i, 0) + 1
        print(d)
        print(d.values())

test = Solution()
test.isAnagram("anagram", "nagaram")