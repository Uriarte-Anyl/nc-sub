class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # stores the value:index

        # i: value, n: index, enumarate gives a tuple (index, value)
        for i, n in enumerate(nums):
          need = target - n # b = target - a: whats left off 
          if need in seen: # if leftover is in the map
            return [seen[need], i] # return (leftover, current)
          seen[n] = i #else add the current      