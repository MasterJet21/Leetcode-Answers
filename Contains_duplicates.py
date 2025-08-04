class Solution:
    def containsDuplicate(self, nums):
        dict = {}
        for i in nums:
            if i not in dict:
                dict.update({i: 1})
            else:
                return True
        return False
