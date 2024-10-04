"""
2220. Minimum Bit Flips to Convert Number

A bit flip of a number x is choosing a bit in the binary
representation of x and flipping it from either 0 to 1 or 1 to 0.

s= 10, g=7. Ans is 3. [ 1010 -> 0111 : needs 3 flips]
-> Here, we just need to find the difference of the digits between two numbers i.e.
an operator that should tell me when both numbers have 0 is 0, both have 1 is 0 , either of it has 1 then 1.
This is XOR operator.

So diff = s^g
Count number of 1's in diff.
using bitwise operators, we can count as:
    while diff!=0:
        cnt += diff & 1
        diff = diff >> 1 #right shift the number
"""
