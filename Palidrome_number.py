class Solution:
    def isPalindrome(self, x):
        new_list = []
        new_list1 = [] 
        x = str(x)
        for j in x:
            if j != "'":
                new_list.append(j)
        print(new_list)
        for i in new_list[::-1]:
            new_list1.append(i)
        print(new_list1)
        if new_list1 == new_list:
            return True
        else:
            return False

#############################################################
#Without converting the integer to a string


# Test cases
s = Solution()
print(s.isPalindrome(-121))  # True