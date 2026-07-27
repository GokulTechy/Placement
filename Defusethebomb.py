from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        for i in range(n):
            total = 0

            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]

            result[i] = total

        return result


if __name__ == "__main__":
    solution = Solution()
    print("Test 1 (code=[5,7,1,4], k=3):", solution.decrypt([5, 7, 1, 4], 3))
    print("Test 2 (code=[1,2,3,4], k=0):", solution.decrypt([1, 2, 3, 4], 0))
    print("Test 3 (code=[2,4,9,3], k=-2):", solution.decrypt([2, 4, 9, 3], -2))
