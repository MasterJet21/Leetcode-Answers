class Solution:
    def smallestEvenMultiple(self, n):
        correct = False
        output = []
        self.n = n
        
        if n == 0:
            return 0
        while correct is False:
            if n % 2 == 0:
                output.append(n)
                correct = True
                return output[0]

            else:
                n = n*2

if __name__ == '__main__':

    test = Solution()
    test1 = Solution()
    test2 = Solution()
    test3 = Solution()
    test4 = Solution()
    print(test.smallestEvenMultiple(0))
    print(test1.smallestEvenMultiple(10))
    print(test2.smallestEvenMultiple(2))
    print(test3.smallestEvenMultiple(5))
    print(test4.smallestEvenMultiple(6))

# e.g.s: 1. 2 and 5(n) ===> 10(Output)
#        2. 2 and 10(n) ===> 10(Output)
#        3. 2 and 3(n) ===> 6(Output)