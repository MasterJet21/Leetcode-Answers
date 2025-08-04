class Solution:
    def searchInsert(self, num, target):
        for i in num:
            if i == target:
                return num.index(i)
            if target < i:
                return num.index(i)
        return(len(num))
            
test = Solution()
print(test.searchInsert([1,3,5,6], 5)) # 2
print(test.searchInsert([1,3,5,6], 2)) # 1
print(test.searchInsert([1,3,5,6], 7)) # 4