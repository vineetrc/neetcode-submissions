class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stack = []

        for i in s:
            if i in ['{', '[', '(']:
                stack.append(i)
            if i in ['}', ']', ')']:
                if not stack:
                    return False
                res = stack.pop() 
                if i == '}' and res == '{':
                    continue
                if i == ']' and res == '[':
                    continue
                if i == ')' and res == '(':
                    continue
                return False
        
        if stack:
            return False
        return True