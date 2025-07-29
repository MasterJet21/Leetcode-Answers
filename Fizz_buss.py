class Solution:
    def fizzBuzz(self, n):
        new_list = []
        i = 1

        while i <= n:

            if i % 3 == 0 and i % 5 == 0:
                new_list.append("FizzBuzz")
            
            elif i % 3 == 0:
                new_list.append("Fizz")
                
            elif i % 5 == 0:
                new_list.append("Buzz")

            elif i % 3 != 0 or i % 5 != 0:
                new_list.append(str(i))


            i += 1

        return new_list
    
test = Solution()  
print(test.fizzBuzz(15))