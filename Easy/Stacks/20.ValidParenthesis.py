class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in brackets.values():  # opening brackets
                stack.append(char)
            elif char in brackets:  # closing brackets
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop()
        
        return not stack  # return True if stack is empty