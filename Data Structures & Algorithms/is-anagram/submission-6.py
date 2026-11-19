class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # inp: s, t: str: O(1) lowercase char
        # oup: bool
        # bru: O(n^2)
        # sor: O(nlogn)
        # t: O(n) s: O(1)

        count_s, count_t = {},{}

        ls, lt = len(s), len(t)

        if ls != lt:
            return False

        for i in range(ls):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        for ch in count_s:
            if count_s[ch] != count_t.get(ch, 0):
                return False
        return True
