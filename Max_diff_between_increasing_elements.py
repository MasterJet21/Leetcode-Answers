class Solution:
    def maximumDifference(self, nums):
        max_diff = []
        for k in range(1, len(nums)):
            a = k - 1
            while a >= 0:
                if nums[k] > nums[a]:
                    max_diff.append(nums[k]-nums[a])
                a -= 1
        if max_diff:
            max_diff = sorted(max_diff, reverse=True)
            return max_diff[0]
    
        else:
            return -1

test = Solution()
test.maximumDifference([1,5,2,10])