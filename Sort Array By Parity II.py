from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n, j = len(nums), 1
        for i in range(0, n, 2):
            if nums[i] % 2:
                while nums[j] % 2:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == "__main__":
    solution = Solution()
    print("Test 1 ([4,2,5,7]):", solution.sortArrayByParityII([4, 2, 5, 7]))
    print("Test 2 ([2,3]):", solution.sortArrayByParityII([2, 3]))
