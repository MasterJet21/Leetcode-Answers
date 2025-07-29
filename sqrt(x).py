class Solution:
    def mySqrt(self, x):
        right = x
        left = 0
        if x == 0:
            return 0
        while left <= right:
            mid = (right+left)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid + 1
            elif mid*mid > x:
                right = mid - 1
            
        return right
    
test = Solution()
print(test.mySqrt(8))