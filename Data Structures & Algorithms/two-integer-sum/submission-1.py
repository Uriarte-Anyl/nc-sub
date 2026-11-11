class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, crnt in enumerate(nums):
            need = target - crnt
            if need in seen:
                return [seen[need], i]
            else:
                seen[crnt] = i