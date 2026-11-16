class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

    #loops if pointers are not colliding
        while L < R:
            while L < R and not self.alphaNum():
                L += 1
            while R > L and not self.alphaNum():
                R -= 1
            #checks if characters are not the same
            if s[L].lower() != s[R].lower():
                return False
            #L & R moves if the condition is not met
            L, R =  L + 1, R -1
        return True

    #checks if the character is alphanumeric
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("b") or
                ord("0") <= ord(c) <= ord("9"))