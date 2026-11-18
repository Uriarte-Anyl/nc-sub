class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # hash map to locate the first integer, lookup O(n)
        # compare the val: nums[i] inside the hashmap, use the key indices
        # [0, 1]: need/diff = target - a: target = a(0) + b(1):    

        seen = {}

        for cur, val in enumerate(nums):
            need = target - val
            if need in seen:
                return [seen[need], cur]
            else:
                seen[val] = cur