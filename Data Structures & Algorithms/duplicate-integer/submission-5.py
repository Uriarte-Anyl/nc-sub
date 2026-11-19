class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # inp: nums[]
        # oup: bool
        # set() avoid duplications

        store = set()

        for i in nums:
            if i in store:
                return True
            store.add(i)
        return False