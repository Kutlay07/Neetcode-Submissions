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
            if p in ["(", "{", "["]:
                stack.append(p)
            elif p in [")", "}", "]"]:
                if not stack:
                    return False
                else:
                    if stack[-1] == close_to_open[p]:
                        stack.pop()
                    else:
                        return False
        return not stack