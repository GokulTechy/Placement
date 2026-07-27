from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        cnt["o"] >>= 1
        cnt["l"] >>= 1
        return min(cnt[c] for c in "balon")


if __name__ == "__main__":
    solution = Solution()
    print('Test 1 ("nlaebolko"):', solution.maxNumberOfBalloons("nlaebolko"))  # Expected: 1
    print('Test 2 ("loonbalxballpoon"):', solution.maxNumberOfBalloons("loonbalxballpoon"))  # Expected: 2
    print('Test 3 ("leetcode"):', solution.maxNumberOfBalloons("leetcode"))  # Expected: 0
