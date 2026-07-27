class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = set(brokenLetters)
        return sum(all(c not in s for c in w) for w in text.split())


if __name__ == "__main__":
    solution = Solution()
    print("Test 1:", solution.canBeTypedWords("hello world", "lo"))  # Expected: 1 (or 0)
    print("Test 2:", solution.canBeTypedWords("leet code", "lt"))  # Expected: 1
    print("Test 3:", solution.canBeTypedWords("this is a test", "abc"))  # Expected: 3
