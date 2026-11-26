class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count [1:1, 2:2, 3:3]
        # [] hold
        # loop k = 2
        # [max(dict, key)]
        # del[max(dict, key)]
        
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        res = []
        for i in range(k):
            res.append(max(count, key = count.get))
            del count[max(count, key = count.get)]
        return res
