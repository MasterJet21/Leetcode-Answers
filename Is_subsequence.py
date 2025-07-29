class Solution:
    def isSubsequence(self, s, t):
        left = 0
        right = 0
        check_list = ''
        while left < len(s) and right< len(t):
            if len(s) == 0:
                return True
            if s[left] == t[right]:
                check_list = check_list + s[left]
                left += 1
                right += 1
            else:
                right += 1
        if check_list == s:
            return True
        else:
            return False

test = Solution()
print(test.isSubsequence("abc", "ahbgdc"))