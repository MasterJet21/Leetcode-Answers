class Solution:
    def minimumOperations(self, nums):
        counter = 0
        for i in nums:
            if i % 3 != 0:
                counter += 1
        print(counter)

test = Solution()
test.minimumOperations([1, 3, 5, 7])