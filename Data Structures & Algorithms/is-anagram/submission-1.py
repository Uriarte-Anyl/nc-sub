class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #one line sorting by using a built-in method
        #t:O(n), s:O(n)

        return sorted(s) == sorted(t)