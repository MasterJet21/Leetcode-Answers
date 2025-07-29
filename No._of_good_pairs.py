class Solution:
    def numIdenticalPairs(self, nums):
        d = {}
        for i in range(len(nums)):
            d.update({i: nums[i]})
        
        

test = Solution()
test.numIdenticalPairs([1,2,3,1,1,3])