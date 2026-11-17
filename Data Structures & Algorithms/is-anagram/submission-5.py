class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram. ab = ba
        #brute force. sort(ab, ba) => ab == ab : O(nlogn)
        #opt sol. "ab", "ba". if len(s) != len(t). {a:2, b:2} == {a:2, b:2}
        #one line sol. return Counter(s) == Counter(t)

        # long sol.
        # if len(s) != len(t):
        #     return False

        # count_s, count_t = {}, {}

        # for i in range(len(s)):
        #     count_s[s[i]] = count_s.get(s[i], 0) + 1
        #     count_t[t[i]] = count_t.get(t[i], 0) + 1

        # for ch in count_s:
        #     if count_s[ch] != count_t.get(ch, 0):
        #         return False
        # return True

        #one line sol. 
        return Counter(s) == Counter(t)