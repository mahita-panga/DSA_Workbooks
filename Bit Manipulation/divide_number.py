"""
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Intuition:
    Key idea: 22/3 is similar to
    express dividend in terms of multipliers of divisor and power
    22 = 3*2^2 + 3*2^1 + 3*2^0

     22               10              4
    -12 (3.2^2)      - 6 (3.2^1)     -3(3.2^0)
    ----            -----            ----
     10               4               1

     Ans = (2^2 + 2^1 + 2^0) = 4+2+1 = 7
->Steps needed:
    Break dividend into multiples of 3 (the divisor) using powers of 2
    Subtract the dividend with the left over number
    find the largest multiple of 3 that fits into 10
    Repeat this until dividend>=divisor.
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        sign = 1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            sign = -1
        num, den= abs(dividend), abs(divisor)
        q = 0
        while num>=den:
            p = 0
            while num >= den<<(p+1) : #(den*2^p)
                p+=1
            q += 1<<p #2^p
            num = num - (den<<p)

        if q==1<<31 and sign==1: #overflow conditions
            return (1<<31) - 1
        elif q==1<<31 and sign==-1:
            return 0-(1<<31)
        else:
            return q if sign==1 else (0-q)
