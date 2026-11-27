class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        prefix = 1

        for n in nums:
            result.append(prefix)
            prefix *= n

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result