class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # output: +1 index: [1,2]. [n, n] = target. 
        # opt sol. l, r pntr. total < target: l + 1, total > target: r - 1

        l, r = 0, len(numbers) - 1

        while l < r: # loops until pntrs meet in the middle
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l + 1, r + 1] # [1-indexed: 0->1, 1->2]
        return [] # fail safe        