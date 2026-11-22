class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}

        for word in strs:
            tally = [0] * 26 # [0,0,0...] for 26 lowercase letters

            for ch in word:
                tally[ord(ch) - ord('a')] += 1 # tally[1(a), 0(b), 1(c)..] "act"

            key = tuple(tally)

            if key not in hmap:
                hmap[key] = []
            hmap[key].append(word)

        return list(hmap.values())