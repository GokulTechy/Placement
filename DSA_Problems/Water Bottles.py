class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange - 1
            ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print("Test 1 (9, 3):", solution.numWaterBottles(9, 3))
    print("Test 2 (15, 4):", solution.numWaterBottles(15, 4))