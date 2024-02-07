class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False
    

a = Solution()
nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
nums = [2,1,5,0,4,6] 
print(a.increasingTriplet(nums))