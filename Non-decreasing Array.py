from itertools import pairwise
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def is_sorted(nums: List[int]) -> bool:
            return all(a <= b for a, b in pairwise(nums))

        n = len(nums)
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            if a > b:
                nums[i] = b
                if is_sorted(nums):
                    return True
                nums[i] = nums[i + 1] = a
                return is_sorted(nums)
        return True


if __name__ == "__main__":
    solution = Solution()
    print("Test 1 ([4, 2, 3]):", solution.checkPossibility([4, 2, 3]))
    print("Test 2 ([4, 2, 1]):", solution.checkPossibility([4, 2, 1]))