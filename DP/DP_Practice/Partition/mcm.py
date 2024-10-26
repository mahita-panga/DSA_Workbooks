from functools import lru_cache

class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        @lru_cache(maxsize=None)
        def util(i,j):
            if i==j:
                return 0
            min_op = float('inf')
            for k in range(i,j):
                steps = arr[i-1]*arr[k]*arr[j] + util(i,k)+util(k+1,j)
                min_op = min(min_op,steps)
            return min_op

        return util(1,N-1)
