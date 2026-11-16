class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force
        #compares each indices
        #first loop will start at index 0
        #second loop will start at index i+1
        #at index 0 it will compare itself onto the next index i+1
        #it will compare until a duplicate is found
        #t: O(n²)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)): #i+1 is used to avoid unecessary pairing
               if nums[i] == nums[j]:
                return True
        return False



