class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #t: O(n), t: O(n)
        #using a hashset, indices will be added and check if there is a duplicate
        # adds memory but optimizes the time operations

        hs = set()
        for n in nums:
            if n in hs:
                return True
            hs.add(n)
        return False