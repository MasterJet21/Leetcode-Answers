#  distinct indices i and j in the array such that nums[i] == nums[j]
# abs(i - j) <= k

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i , val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i
        return False
    
test = Solution()
test.containsNearbyDuplicate([1,2,3,1], 3)