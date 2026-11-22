class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for cur, val in enumerate(nums):
            need = target - val
            
            if need in seen:
                return [seen[need], cur]
            else:
                seen[val] = cur