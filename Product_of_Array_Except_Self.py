class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = nums[i -1] * result[i -1]
        
        right = 1
        for i in reversed(range(len(nums))):
            result[i] *= right
            right = nums[i] * right
        
        return result


a = Solution()
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]

print(a.productExceptSelf(nums))