
| Operator | Name |      Description                      |
|----------|------|---------------------------------------|
|     &    | AND  |  1 if both bits are 1|
|    \|    | OR   |  1 if one of two bits is 1|
|     ^    | XOR  |  1 if only one of two bits is 1, cancels out for even # of 1's|
|     ~    | NOT  |  Inverts all the bits                 |
|    <<    |  Left shift | Shifts left by pushing zeros in from the right |
|    >>    |  Right shift | Shifts right by pushing copies of the leftmost bit in from the left |

Common bit manipulation techniques:
* `<<` (left shift) is often used as a multiplication by powers of 2.
* `>>` (right shift) is often used as a division by powers of 2.

- 2^n = 1>>n, x*2^n = x>>n
- n//2 = n<<1, n//2^x = n<<x
- n%2 = n&1  // if a number has last bit as 1, it is odd and hence returns 1 else 0.`


1. Check if i-th bit is set: `num & (1 << i) != 0`
- (1 << i) creates a number with only the i-th bit set, AND with num is non-zero only if i-th bit in num is set

2. Set i-th bit: `num = (1 << i)`
- (1 << i) creates a number with only the i-th bit set, assigning it to num

3. Clear i-th bit: `num &= ~(1 << i)`
- ~(1 << i) creates a number with all bits set except the i-th, AND with num clears only the i-th bit

4. Toggle i-th bit: `num ^= (1 << i)`
- (1 << i) creates a number with only the i-th bit set, XOR with num flips only the i-th bit

5. Get rightmost 1-bit: `num & -num`
- -num is the two's complement, AND with num isolates the rightmost 1-bit

6. Remove rightmost 1-bit: `num & (num - 1)`
- (num - 1) has all bits right of rightmost 1 flipped, AND with num removes only the rightmost 1-bit

7. Check if power of 2: `num & (num - 1) == 0`
- If a number is power of 2, binary rep. is 1000.. and n-1 is 0111.., AND is hence 0


Remember:
- Bitwise operations are typically faster than arithmetic operations
- They're useful for tasks like manipulating flags, optimizing space usage, and solving certain types of problems efficiently
