class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram: ab = ba: same characters, no order
        #output: ab = ba: True, ab = ca: False
        #input: s, t = ab, ba
        #brute: sorting O(nlogn): ab = ab
        #easier: Counter() => map & checker
        
        # manual sol.
        # mS, mT = {},{}

        # for key in range(len(s)):
        #     mS[s[key]] = mS.get(s[key], 0) + 1
        #     mT[t[key]] = mT.get(t[key], 0) + 1
        
        # for val in mS:
        #     if mS[val] != mS.get(val, 0):
        #         return False
        # return True

        return Counter(s) == Counter(t)