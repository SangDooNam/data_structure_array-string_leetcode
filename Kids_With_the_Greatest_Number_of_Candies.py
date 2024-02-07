class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = max(candies)
        return [True if candy + extraCandies >= greatest else False for candy in candies ]


a = Solution()
candies = [2,3,5,1,3]
extraCandies = 3

# candies = [4,2,1,1,2]
# extraCandies = 1

# candies = [12,1,12]
# extraCandies = 10


print(a.kidsWithCandies(candies, extraCandies))