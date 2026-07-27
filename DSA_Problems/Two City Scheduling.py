from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) >> 1
        return sum(costs[i][0] + costs[i + n][1] for i in range(n))


if __name__ == "__main__":
    solution = Solution()
    print("Test 1:", solution.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))  # Expected: 110
    print("Test 2:", solution.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [540, 341], [173, 638]]))  # Expected: 1859