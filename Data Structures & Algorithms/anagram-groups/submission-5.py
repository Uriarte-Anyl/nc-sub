class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            tally = [0] * 26 # [0,0,0...] for 26 lowercase letters

            for ch in s:
                tally[ord(ch) - ord('a')] += 1 # tally[1(a), 0(b), 1(c)..] "act"

            k = tuple(tally)
            res[k].append(s) # res[[1, 0, 1...] : ["act"]]

        return list(res.values())

