class Solution:
    def firstUniqChar(self, s):
        d = {}
        for i in s:
            if i not in d:
                d.update({i: 1})
            else:
                d[i] += 1

        for j in d:
            if d[j] == 1:
                return s.find(j)

        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))