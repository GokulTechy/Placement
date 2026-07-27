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
    print(solution.isIsomorphic("egg", "add"))
    print(solution.isIsomorphic("foo", "bar"))
    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("badc", "baba"))    