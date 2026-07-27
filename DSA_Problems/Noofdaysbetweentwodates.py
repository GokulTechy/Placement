class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeap(year):
            return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

        def countDates(date):
            y, m, d = map(int, date.split("-"))
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            days = (y - 1) * 365 + (y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400

            for i in range(m - 1):
                days += months[i]
                if i == 1 and isLeap(y):
                    days += 1
            return days + d

        return abs(countDates(date1) - countDates(date2))


if __name__ == "__main__":
    solution = Solution()
    print(solution.daysBetweenDates("2020-01-01", "2020-01-10"))