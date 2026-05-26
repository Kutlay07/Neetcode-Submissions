class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
                
            if len(stack) >= 2:
                if i == "+":
                    num = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(num)

                elif i == "*":
                    num = stack[-1] * stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(num)


                elif i == "-":
                    num = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(num)
                    

                elif i == "/":
                    num = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(num)

        return stack[-1]