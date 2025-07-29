##################################################Using another list###########################################################
# class Solution:
#     def removeDuplicates(self, nums):
#         container = []
#         b = 0
#         for i in nums:        
#             if i not in container:
#                 container.append(i)     
#                 b += 1
            
#         a = len(nums) - len(container)
#         for j in range(0, a):
#             container.append('_')

#         print(container)
#         return container

# test = Solution()
# test.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

##################################################Within the same list###########################################################

class Solution:
    def removeDuplicates(self, nums):
        a = 0
        b = 0
        while a <= len(nums)-2 and b <= len(nums)-2:
            if len(nums) % 2 == 1: #(Odd numbers)
                if nums[a] == nums[a+1]:
                    nums[a] = '_'
                    a += 1
                else:
                    a += 1
        
            if len(nums) % 2 == 0: #(even numbers)
                if nums[b] == nums[b+1]:
                    nums[b] = '_'
                    b += 1
                else:
                    b += 1

        new_list = []

        for i in nums:
            if i != '_':
                new_list.append(i)

        while nums: 
                nums.pop(0)
        for j in new_list:
            nums.append(j)
        # for d in range(0, c):
        #     nums.append('_')
        print(nums)
        return len(nums)

test = Solution()
print(test.removeDuplicates())


# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
