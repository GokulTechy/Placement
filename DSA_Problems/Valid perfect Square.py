class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


if __name__ == "__main__":
    solution = Solution()
    print("Test 1 (16):", solution.isPerfectSquare(16))  # Expected: True
    print("Test 2 (14):", solution.isPerfectSquare(14))  # Expected: False