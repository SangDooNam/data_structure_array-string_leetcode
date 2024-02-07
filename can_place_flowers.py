class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        new = [0] + flowerbed + [0]
        count = 0
        
        for i in range(1, len(new) - 1):
            if new[i -1] == 0 and new[i] == 0 and new[i + 1] == 0:
                new[i] = 1
                count += 1
        
        if count >= n:
            return True
        else:
            return False


a = Solution()

flowerbed = [1,0,0,0,1]
n = 1
flowerbed = [1,0,0,0,1]
n = 2

print(a.canPlaceFlowers(flowerbed, n))