class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) >> 1
            if (1 + mid) * mid // 2 <= n:
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    solution = Solution()
    print("Test 1 (5):", solution.arrangeCoins(5))  # Expected: 2
    print("Test 2 (8):", solution.arrangeCoins(8))  # Expected: 3
