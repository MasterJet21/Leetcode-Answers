class Solution:
    def maxAdjacentDistance(self, nums):
        list_of_diff = []
        leng = len(nums)
        for i in range(leng-1):
            if nums[i]<nums[i+1]:
                diff = nums[i+1]-nums[i]
                list_of_diff.append(diff)
            else:
                diff = nums[i]-nums[i+1]
                list_of_diff.append(diff)

        if nums[leng-1]<nums[0]:
            diff2 = nums[0]-nums[leng-1]
            list_of_diff.append(diff2)
        
        else:
            diff2 = nums[leng-1]-nums[0]
            list_of_diff.append(diff2)

        list_of_diff = sorted(list_of_diff,reverse=True)
        return list_of_diff[0]

test = Solution()
test.maxAdjacentDistance([1,2,4])