class Solution:
    def removeElement(self, nums, val):
        new_list = []
        c = 0
        for i in nums:
            if i != val:
                new_list.append(i)
                print(new_list)
                c += 1
        d = len(nums)-c
        for a in range(0, len(nums)):
            nums.pop()
            print(nums)
        for j in new_list:
            nums.append(j)
        for b in range(0, d):
            nums.append('_')
        print(nums)
        return c

test = Solution()
print(test.removeElement([0,1,2,2,3,0,4,2], 2))