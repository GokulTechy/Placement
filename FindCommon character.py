from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for w in words:
            t = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], t[c])
        return list(cnt.elements())


if __name__ == "__main__":
    solution = Solution()
    print("Test 1:", solution.commonChars(["bella", "label", "roller"]))
    print("Test 2:", solution.commonChars(["cool", "lock", "cook"]))