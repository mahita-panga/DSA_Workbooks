""" https://leetcode.com/problems/sum-of-subarray-minimums/description/
find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Bruteforce - find the subarrays possible and min of each and get sum - O(n^2) to find subarray i.e O(n(N+1)/2)
and O(n) -min in each subarray -- O(n^3)

Optimal - Instead of generating subarray and finding min, if we can find how many subarrays is arr[i] the minimum, we can find the ans
For every arr[i]:
	•	Let left[i] = number of consecutive elements on the left where arr[i] is strictly less.
	•	Let right[i] = number of consecutive elements on the right where arr[i] is less than or equal.
	<= here because this number will be the first min to be considered in those subarrays

number of subarrays where arr[i] is the minimum = left[i] * right[i]

Thus use a monotonic increasing stack to find left and right for each i:
	•	prev_less[i]: index of previous element less than arr[i]
	•	next_less[i]: index of next element strictly less than arr[i]

Then:
	•	left[i] = i - prev_less[i] (num of subarrays on lef side where i is min)
	•	right[i] = next_less[i] - i (num of subarrays on right side where i is min)

Ex:  arr = [3, 1, 2, 4]

Let’s compute for each element:

For arr[1] = 1:
	•	Subarrays where 1 is the minimum:
	•	Left: [3, 1] → prev less = -1 → left = 1 - (-1) = 2
	•	Right: [1, 2, 4] → next less = None → right = 4 - 1 = 3
	•	Count = 2 × 3 = 6 → Contribution = 6 × 1 = 6

Do this for all, sum contributions.

Total = 3×1 + 1×6 + 2×2 + 4×1 = 17
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        left = [0] * n
        stack = []

        #LEFT COUNT
        for i in range(n):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            # if no min, then left[i] = I+1 else i-stack[i]
            left[i] = i + 1 if not stack else (i - stack[-1])
            stack.append(i)

        right = [0] * n
        stack = []
        # RIGHT COUNT
        for i in range(n - 1, -1, -1):

            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            # if no min, then right[i] = n-1 else (end min - curr) stack[-1]-i
            # 	•	If there’s no next smaller element after i:
            #    → right[i] = n - i (i.e., from index i to end)
            #   •	If the next smaller element is at index j:
            #    → right[i] = j - i (i.e., from i to j-1)
            right[i] = n - i if not stack else (stack[-1] - i)
            stack.append(i)

        MOD = 10**9 + 7
        ans = 0

        for i in range(n):
            ans = (ans + left[i] * arr[i] * right[i]) % MOD
        return ans
