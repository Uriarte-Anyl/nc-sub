class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1st sol. using a hashmap
        #t: O(n) s: O(k); 26 alph char doesnt grow just repeats
        
        m_s, m_t =  {},{}

        #early check if the length of s,t is the same
        if len(s) != len(t):
            return False
        
        #adds k:v pairs in both hashmaps and increments if shows duplication
        for i in range(len(s)):
            m_s[s[i]] = m_s.get(s[i], 0) + 1
            m_t[t[i]] = m_t.get(t[i], 0) + 1
        
        #compares the n values of both hashmaps
        for j in m_s:
            if m_s[j] != m_t.get(j, 0):
                return False
        return True
        