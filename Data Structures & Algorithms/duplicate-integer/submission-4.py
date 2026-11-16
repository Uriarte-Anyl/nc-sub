class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #output: true if there is a duplicate in the array
        #input: array of nums with or without duplicates
        #brute: check every possible pair O(n²)
        #sort(): so that the possible duplicates are adjacent
        #opt sol: set() t: O(n) s: O(n)

        new = set()

        for i in nums:
            if i in new:
                return True
            else:
                new.add(i)
        return False