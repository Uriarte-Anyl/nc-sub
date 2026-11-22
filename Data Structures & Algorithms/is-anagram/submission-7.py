class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # c: return Counter(s) == Counter(t)
        
        ms, mt = {}, {}
        ls, lt = len(s), len(t)

        if ls != lt:
            return False
        
        for i in range(ls):
            ms[s[i]] = ms.get(s[i], 0) + 1
            mt[t[i]] = mt.get(t[i], 0) + 1

        for ch in ms:
            if ms[ch] != mt.get(ch, 0):
                return False
        return True
