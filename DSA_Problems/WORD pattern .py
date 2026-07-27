class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ws = s.split()
        if len(pattern) != len(ws):
            return False
        d1 = {}
        d2 = {}
        for a, b in zip(pattern, ws):
            if (a in d1 and d1[a] != b) or (b in d2 and d2[b] != a):
                return False
            d1[a] = b
            d2[b] = a
        return True


if __name__ == "__main__":
    solution = Solution()
    print("Test 1:", solution.wordPattern("abba", "dog cat cat dog"))  # Expected: True
    print("Test 2:", solution.wordPattern("abba", "dog cat cat fish"))  # Expected: False
    print("Test 3:", solution.wordPattern("aaaa", "dog cat cat dog"))  # Expected: False
