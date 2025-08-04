class Solution:
    def majorityElement(self, nums):
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        max_count = 0
        max_key = None

        for j in dict:
            if dict[j] > max_count:
                max_count = dict[j]
                max_key = j

        return max_key

test = Solution()
print(test.majorityElement([3,2,3]))