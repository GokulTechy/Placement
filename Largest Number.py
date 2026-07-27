from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(v) for v in nums]
        nums.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        return "0" if nums[0] == "0" else "".join(nums)


if __name__ == "__main__":
    solution = Solution()
    print("Test 1 ([10, 2]):", solution.largestNumber([10, 2]))  # Expected: "210"
    print("Test 2 ([3, 30, 34, 5, 9]):", solution.largestNumber([3, 30, 34, 5, 9]))  # Expected: "9534330"
