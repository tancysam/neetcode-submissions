class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operationStack = []
        currentEval = None
        for ch in tokens:
            if ch.isnumeric():
                operationStack.append(ch)
            else:
                while len(operationStack) > 0:
                    if currentEval:
                        currentEval = self.operation(ch, currentEval, operationStack.pop(0))
                    else:
                        currentEval = operationStack.pop(0)
        
        return currentEval


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
            return num1 * num2
    

