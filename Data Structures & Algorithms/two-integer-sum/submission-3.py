class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #output: nums[i] + nums[j] == target
        #brute: iterate through the array O(n²)

        m = {}

        for i, current in enumerate(nums): #(val, index): (3, 0)
            need = target - current

            if need in m:
                return [m[need], i] #returns [v, index]: [0, 1]
            else:
                m[current] = i #adds k: current/value, v: index in map: map[0] = 3
            