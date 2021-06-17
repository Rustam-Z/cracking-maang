class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num != 0:
            num = num / 2 if num % 2 == 0 else num - 1    
            counter += 1
        return counter

        # digits = f'{num:b}'
        # return digits.count('1') - 1 + len(digits)

num = 14 
sol = Solution()
print(sol.numberOfSteps(num))

'''
14  ITERATIONS
7   1
6   2
3   3
2   4
1   5
0   6

NOT WORKING (: 
num = num / 2 if num % 2 == 0 else num - 2   
14  EXPLANATION     ITERATIONS with counter, crazy code)
8   7+1             1
5   4+1             2
4   3+1             3
3   2+1             4
2   1+1             5

'''
