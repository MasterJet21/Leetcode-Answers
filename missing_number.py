class Solution:
    def missingNumber(self, nums):
        leng = len(nums)
        d1 = {}
        d2 = {}
        for i in range(leng+1):
            d1.update({i: 1})
        for j in nums:
            d2.update({j: 1})
        
        for k in d1:
            if k not in d2:
                return k