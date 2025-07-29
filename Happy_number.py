class Solution:
    def isHappy(self, n):
        new_n = 0
        new_list = []
        check = True
        counter = 0
        if n >= 0:
            for i in str(n):
                new_list.append(i)

            while new_n != 1 and counter < 100:
                for j in str():
                    .append(j)

                for i in new_list:
                    i = int(i)
                    new_n = new_n + (i * i)
                    counter += 1
                if new_n != 1:
                     = new_n
                
                if new_n == 1:
                    return True
        else:
            return False

test = Solution()
print(test.isHappy(19))