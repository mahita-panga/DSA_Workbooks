
| Operator | Name |      Description                      |
|----------|------|---------------------------------------|
|     &    | AND  |  if both bits are 1                   |
|    \|    | OR   |  if one of two bits is 1              |
|     ^    | XOR  |  if only one of two bits is 1         |
|     ~    | NOT  |  Inverts all the bits                 |
|    <<    |L.shift| Shifts left by pushing zeros in from the right |
|    >>    |R.shift| Shifts right by pushing copies of the leftmost bit in from the left |

Common bit manipulation techniques:
1. Check if i-th bit is set: `num & (1 << i) != 0`
2. Set i-th bit: `num = (1 << i)`
3. Clear i-th bit: `num &= ~(1 << i)`
4. Toggle i-th bit: `num ^= (1 << i)`
5. Get rightmost 1-bit: `num & -num`
6. Remove rightmost 1-bit: `num & (num - 1)`
7. Check if power of 2: `num & (num - 1) == 0`

Remember:
- Bitwise operations are typically faster than arithmetic operations
- They're useful for tasks like manipulating flags, optimizing space usage, and solving certain types of problems efficiently
