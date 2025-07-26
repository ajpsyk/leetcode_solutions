from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands_stack = []
        for token in tokens:
            if token == "+":
                operands_stack.append(operands_stack.pop() + operands_stack.pop()) 
            elif token == "-":
                second = operands_stack.pop()
                operands_stack.append(operands_stack.pop() - second) 
            elif token == "*":
                operands_stack.append(operands_stack.pop() * operands_stack.pop()) 
            elif token == "/":
                second = operands_stack.pop()
                operands_stack.append(operands_stack.pop() // second) 
            else:
                operands_stack.append(int(token))
        return operands_stack.pop()