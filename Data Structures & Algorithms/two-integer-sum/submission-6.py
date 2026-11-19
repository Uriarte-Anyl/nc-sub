class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # inp: p = t - p[v]
        # oup: [p, p]: p + p = t
        # t: O(n) s: O(1)

        seen = {}

        for cur, val in enumerate(nums):
            need =  target - val

            if need in seen:
                return [seen[need], cur]

            else:
                seen[val] = cur
            