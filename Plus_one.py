class Solution:
    def plusOne(self, digits):
        number = ''
        ls = []
        new_ls = []
        for i in range(len(digits)):
            number = number + (str(digits[i]))

        number = int(number)
        number = number + 1
        number = str(number)  # Cannot iterate through an integer
        for j in number:
            ls.append(j)
        for s in ls:
            s = int(s)
            new_ls.append(s)
        return new_ls


test = Solution()
print(test.plusOne([1,2,3,4,5,6,7,8,9]))