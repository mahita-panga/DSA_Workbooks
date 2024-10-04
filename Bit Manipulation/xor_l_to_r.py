"""
There is a pattern to xor of numbers:
    N=1 , 1          =1
    N=2 , 1^2        =3
    N=3 , 1^2^3      =0
    N=4 , 1^2^3^4    =4

    N=5 ,(1^2^3)^4^5 =1
    N=6, 4^5^6       =7
    N=7, 4^5^6^7     =0
    N=8, 0^8         =8

So, we see that when
N%4 = 1, then xor = 1,
N%4 = 2, then xor = N+1
N%4 = 3, then xor = 0
N%4 = 0, then xor = N


FOR finding the xor in range l->r,
instead of iterating from l->r, we can do:
    xor(l-1): 1^2^3^..^l-1
    xor(r): 1^2^3^..^l-1^l..^r

    when we do xor of both, we will be left with xor from l->r as remaining will be cancelled out.

"""
class Solution:
    def findXOR(self, l, r):
        # Code here
        def xor_of_n(n):
            if n%4==0:
                return n
            elif n%4==1:
                return 1
            elif n%4==2:
                return n+1
            else:
                return 0

        lxor = xor_of_n(l-1) #compute till l-1
        rxor = xor_of_n(r)
        return lxor^rxor
