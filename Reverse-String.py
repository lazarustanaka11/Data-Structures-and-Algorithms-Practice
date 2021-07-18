class Solution:
    def reverse(self, x: int) -> int:

        def divide(num,d):
            return int(num*1.0/d)
        def mod(num,m):
            if num < 0:
                return num % -m
            else:
                return num%m
            
        range_max= 2**31 -1
        range_min= -2**31

        result= 0
        while x != 0:
            pop = mod(x,10)
            x= divide(x,10)
            if result>divide(range_max,10) or (result==divide(range_max,10) and pop>7):
                return 0
            if result<divide(range_min,10) or (result==divide(range_min,10) and pop<-8):
                return 0
            result = result *10 + pop
        return result
