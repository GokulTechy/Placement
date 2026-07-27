from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        while candies:
            ans[i % num_people] += min(candies, i + 1)
            candies -= min(candies, i + 1)
            i += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.distributeCandies(7, 4))
    print(solution.distributeCandies(10, 3))