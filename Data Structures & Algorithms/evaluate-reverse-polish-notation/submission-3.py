class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operationStack = []

        for ch in tokens:
            if ch not in "+-*/":
                operationStack.append(ch)
            else:
                num1 = operationStack.pop()
                num2 = operationStack.pop()
                operationStack.append(self.operation(ch,num2,num1))

        
        return int(operationStack[0])


    def operation(self,operand,num1,num2):
        num1 = int(num1)
        num2 = int(num2)

        if operand == "+":
            return num1 + num2
        elif operand == "-":
            return num1 - num2
        elif operand == "*":
            return num1 * num2
        elif operand == "/":
            return num1 / num2
    

