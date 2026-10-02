class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for p in s:
            if p in close_to_open:
                if stack and stack[-1] == close_to_open[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return not stack