class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # inp: strs[]
        # oup: [strs[], strs[]]
        
        book = defaultdict(list)
        lo_let = 26

        for s in strs:
            count = [0] * lo_let

            for ch in s:
               count[ord(ch) - ord('a')] += 1

            key = tuple(count)
            book[key].append(s)
        
        return list(book.values())