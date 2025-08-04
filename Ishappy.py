class Solution:
    def isHappy(self, n):
        new_n = 0
        new_list = []
        check = False
        counter = 0

        if n >= 0:
            for i in str(n):
                new_list.append(int(i))
            print(new_list)
            
            while check is False and counter <= 6:
                for j in new_list:
                    new_n = new_n + (j*j)
                new_list = []
                for k in str(new_n):
                    new_list.append(int(k))
                if new_n == 1:
                    check = True
                else:
                    check = False
                    counter += 1
                new_n = 0

            return check
        
        else:
            return check

test = Solution()
test.isHappy(19)