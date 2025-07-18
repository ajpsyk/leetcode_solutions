class Solution:
    def isValid(self, s: str) -> bool:
        # hashMap, closed parens as key, open parents as value
        hashMap = {")":"(", "}":"{","]":"["}
        stack = []
        top = len(stack) - 1
        # iterate over input string
        for c in s:
            # if char in hashMap keys
            if c in hashMap:
                # if stack has values and top of stack is value
                if stack and stack[top] == hashMap[c]:
                    # pop stack
                    stack.pop()
                # else
                else:
                    # return false
                    return False
            # else
            else:
                # push char to stack
                stack.append(c)
        # return if stack is empty
        return len(stack) == 0