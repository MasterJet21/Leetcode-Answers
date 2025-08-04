class Solution:
    def isValid(self, s):
        check_list = []
        for i in s:
            if i == '(':
                check_list.append(i)
            if i == '[':
                check_list.append(i)
            if i == '{':
                check_list.append(i)
            if i == ')':
                if len(check_list) == 0 or check_list[-1] != '(':
                    return False
                check_list.pop()
            if i == ']':
                if len(check_list) == 0 or check_list[-1] != '[':
                    return False
                check_list.pop()
            if i == '}':
                if len(check_list) == 0 or check_list[-1] != '{':
                    return False
                check_list.pop()
        if len(check_list) == 0:
            return True
        else:
            return False
test = Solution()
print(test.isValid("("))  # True