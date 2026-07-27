import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = set(banned)
        p = Counter(re.findall(r"[a-z]+", paragraph.lower()))
        return next(word for word, _ in p.most_common() if word not in s)


if __name__ == "__main__":
    solution = Solution()
    p1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    b1 = ["hit"]
    print("Test 1:", solution.mostCommonWord(p1, b1))  # Expected: "ball"

    p2 = "a."
    b2 = []
    print("Test 2:", solution.mostCommonWord(p2, b2))  # Expected: "a"