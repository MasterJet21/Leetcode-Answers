class Solution:
    def twoSum(self, nums, target: int):
        i = 0
        j = 1
        # if target =
        while i < len(nums):
            while j < len(nums):
                if nums[i]+nums[j] == target:
                    return (i, j)
                else:
                    j = j + 1
            i = i + 1
            j = i + 1

test = Solution()
print(test.twoSum([2,1,9,4,4,56,90,3], 8))











