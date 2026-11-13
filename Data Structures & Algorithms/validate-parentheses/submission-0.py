class Solution:
    def isValid(self, s: str) -> bool:
        opens = set('({[')
        closeToOpen = {')': '(', '}': '{', ']': '[',}
        unusedOpens = []

        for bracket in s:
            if bracket in opens:
                unusedOpens.append(bracket)
            else:
                matchingOpen = closeToOpen[bracket]
                if len(unusedOpens) > 0 and matchingOpen == unusedOpens[-1]:
                    unusedOpens.pop()
                else:
                    return False
        return len(unusedOpens) == 0