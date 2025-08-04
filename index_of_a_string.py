class Solution:
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        
test = Solution()
print(test.strStr("hello", "ll"))  # Output: 2