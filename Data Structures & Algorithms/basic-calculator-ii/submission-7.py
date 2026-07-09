class Solution:
    def calculate(self, s: str) -> int:
        
        s = s.replace(" ", "")
        print(s)

        sign = "+"
        num = ""
        stack = []
        for c in s:
            if c in '0123456789':
                num +=c
            elif c in "+-/*":
                # print(stack)
                if sign == "+":
                    stack.append(int(num))
                if sign == "-":
                    stack.append(-1 * int(num))
                if sign == "*":
                    val = stack.pop()
                    stack.append(val*int(num))
                if sign == "/":
                    val = stack.pop()
                    stack.append(int(val / int(num)))
                sign = c
                num = ""
        
        if sign == "+":
            stack.append(int(num))
        if sign == "-":
            stack.append(-1 * int(num))
        if sign == "*":
            val = stack.pop()
            stack.append(val*int(num))
        if sign == "/":
            val = stack.pop()
            stack.append(int(val / int(num)))

        # print(stack)
        return int(sum(stack))