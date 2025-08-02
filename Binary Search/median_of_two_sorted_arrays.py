"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
You are given two sorted arrays nums1 and nums2, and you need to find the median of the combined sorted array in O(log(min(n, m))) time.

	•	Brute-force merging → O(n + m), but this won’t scale for large arrays.
	•	Since both arrays are sorted, we can perform binary search to find the correct partition point in both arrays such that:
    	•	Elements on the left half ≤ elements on the right half.
    	•	Size of left half = size of right half (or +1 if odd total)
    -> Binary search is done to find the right partition and not the number

Binary search on smaller array to find the partition,
   	Where:
	•	maxLeft1 = nums1[i - 1], minRight1 = nums1[i]
	•	maxLeft2 = nums2[j - 1], minRight2 = nums2[j]
	•	j = (len1 + len2 + 1)//2 - i → to ensure left half has correct number of elements

TC -  O(log(min(n, m)))
"""
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        n1, n2 = len(a), len(b)
        # if n1 is bigger swap the arrays:
        if n1 > n2:
            return self.findMedianSortedArrays(b, a)

        n = n1 + n2  # total length
        left = (n1 + n2 + 1) // 2  # length of left half
        # apply binary search:
        low, high = 0, n1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            # calculate l1, l2, r1, and r2;
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            if mid1 - 1 >= 0:
                l1 = a[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = b[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

            # eliminate the halves:
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0
