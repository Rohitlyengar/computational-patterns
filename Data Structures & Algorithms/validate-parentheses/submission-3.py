class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.pop()
                    
        return len(stack) == 0
