class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthPair= { ")":"(", "]":"[" , "}":"{" }

        for c in s:
            if c in paranthPair: #if char is closing paranthesis then check for pairing
                if stack and stack[-1]==paranthPair[c]:
                    stack.pop()
                else:
                    return False
            else: #if char is opening then add it to stack
                stack.append(c)
        if not stack:
            return True
        else:
            return False
