class Solution:
    def removeDuplicates(self, nums):
        firstpointer = 1
        secondpointer = 2
        refcopy = nums[:]
        while secondpointer <= len(nums)-1:
            if nums[secondpointer] == nums[firstpointer]:
                if nums[firstpointer-1] == nums[firstpointer]:
                    nums[secondpointer] = nums[-1]+1
                    nums.sort()
                else:
                    firstpointer += 1
                    secondpointer += 1
            else:
                firstpointer += 1
                secondpointer += 1

        for i in range(len(nums)):
            if nums[i] not in refcopy:
                return i

test = Solution()
test.removeDuplicates([1,1])