from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = len(moves)
        cnt = [0] * 8
        for k in range(n - 1, -1, -2):
            i, j = moves[k]
            cnt[i] += 1
            cnt[j + 3] += 1
            if i == j:
                cnt[6] += 1
            if i + j == 2:
                cnt[7] += 1
            if any(v == 3 for v in cnt):
                return "B" if k & 1 else "A"
        return "Draw" if n == 9 else "Pending"


if __name__ == "__main__":
    solution = Solution()
    print("Test 1:", solution.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))  # "A"
    print("Test 2:", solution.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))  # "B"
    print("Test 3:", solution.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))  # "Draw"
