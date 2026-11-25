class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set() => [2,20,4,10,3,4,5]: [2, 4, 3, 5]: 4
        # set() => [0, 3, 2, 5, 4, 6]: 7

        store = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in store:
                next_num = num + 1
                length = 1
                while next_num in store:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest
