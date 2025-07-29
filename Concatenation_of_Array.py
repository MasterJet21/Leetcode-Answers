class Solution:
    def getConcatenation(self, nums):
        self.nums = nums
        new_array = []
        check = 0
        while check < 2:
            for i in nums:
                new_array.append(i)
            check += 1
        
        return new_array
    
test = Solution()
print(test.getConcatenation([1,3,2,1]))