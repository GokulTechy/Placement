from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] != nums[mid ^ 1]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


if __name__ == "__main__":
    solution = Solution()
    print("Test 1:", solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))  # Expected: 2
    print("Test 2:", solution.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))  # Expected: 10
