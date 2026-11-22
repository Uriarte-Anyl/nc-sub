class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # bf: n0 = n1, n0 = n2...
        # os: s = [] n0 in s r: T, e add s..

        dup = set()

        for i in nums:
            if i in dup:
                return True
            else:
                dup.add(i)
        return False
        