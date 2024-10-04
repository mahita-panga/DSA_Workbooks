"""
https://www.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1

This function finds two odd occurring numbers in an array
Input: arr - the input array, N - the size of the array
Output: A tuple containing the two odd occurring numbers

-> XOR all elements in the array
XOR of two same numbers is 0, so all pairs will cancel out
leaving only the XOR of the two odd occurring numbers

-> Find the rightmost set bit in the XOR result
This bit will be set in one odd number and unset in the other

-> Divide all numbers in the array into two groups:
1. Numbers with the rightmost set bit
2. Numbers without the rightmost set bit

XOR all numbers in each group separately
This will give us the two odd occurring numbers
"""

class Solution:
    def twoOddNum(self, arr, N):
        # code here
        xorr = 0
        for i in arr:
            xorr ^= i

        right_set_bit = (xorr&xorr-1)^xorr #Isolating the right most set bit
        #This bit is the rightmost that differentiates between the two numbers,

        b1 = 0
        b2 = 0
        for i in arr:
            if i&right_set_bit:
                b1 ^= i
            else:
                b2 ^= i

        return b1,b2
