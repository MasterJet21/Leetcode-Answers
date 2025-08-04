class Solution:
    def twoSum(self, numbers, target):
        leng = len(numbers)
        middle = leng//2
        total = 0

        while numbers[middle] > target and total != target:
            numbers = numbers[:middle]
            middle = (len(numbers)-1)//2
            for i in numbers:
                total += i
            if total == target:
                return [1, 2]
            total = 0

        left = 0
        right = len(numbers)-1

        while left < right:
            currentsum = numbers[left]+numbers[right]
            if currentsum == target:
                return [left+1, right+1]
            elif currentsum < target:
                left += 1
            elif currentsum > target:
                right -= 1

        if target < numbers[0]:
            return None

test = Solution()
print(test.twoSum([-1,-1,1,1,1,1,1,1,1], -2))