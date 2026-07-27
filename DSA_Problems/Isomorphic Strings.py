class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for a, b in zip(s, t):
            if (a in d1 and d1[a] != b) or (b in d2 and d2[b] != a):
                return False
            d1[a] = b
            d2[b] = a
        return True


if __name__ == "__main__":
    solution = Solution()
    print("Test 1 ('egg', 'add'):", solution.isIsomorphic("egg", "add"))
    print("Test 2 ('foo', 'bar'):", solution.isIsomorphic("foo", "bar"))
    print("Test 3 ('paper', 'title'):", solution.isIsomorphic("paper", "title"))
    print("Test 4 ('badc', 'baba'):", solution.isIsomorphic("badc", "baba"))
