class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums) - 1

        while lb <= ub:
            mid = (lb + ub) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[lb] <= nums[mid]:
                if nums[lb] <= target < nums[mid]:
                    ub = mid - 1  # Search left
                else:
                    lb = mid + 1  # Search right
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[ub]:
                    lb = mid + 1  # Search right
                else:
                    ub = mid - 1  # Search left

        return -1
