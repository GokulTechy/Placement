class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = set(brokenLetters)
        return sum(all(c not in s for c in w) for w in text.split())


if __name__ == "__main__":
    solution = Solution()
    print(solution.canBeTypedWords("hello world", "lo"))
    print(solution.canBeTypedWords("leet code", "lt"))
    print(solution.canBeTypedWords("this is a test", "abc"))    