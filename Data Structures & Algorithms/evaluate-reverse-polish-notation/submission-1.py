class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        input: tokens - list of strings: a valid arithmetic expression in Reverse Polish Notation (operators follow operands)
        output: integer: calculate the evaluation of the expression
        constraints: division always truncates toward zero (floor)
        edge cases: 
        
        idea:
        - use a stack to store operands
        - once we hit an operator (+, -, * or /), incrementally pop from the stack and *push that value to the stack?

        how would divide work
        [1,2,+,3,/]
        ((1 + 2) / 3)
        [1,2]
        [3,3]
        [1]
        """

        operands = []
        for token in tokens:
            if token == '+':
                operands.append(operands.pop() + operands.pop())
            elif token == '-':
                a, b = operands.pop(), operands.pop()
                operands.append(b - a)
            elif token == '*':
                operands.append(operands.pop() * operands.pop())
            elif token == '/':
                a, b = operands.pop(), operands.pop()
                operands.append(int(float(b) / a))
                    
            else:
                operands.append(int(token))

        return operands[0]
        