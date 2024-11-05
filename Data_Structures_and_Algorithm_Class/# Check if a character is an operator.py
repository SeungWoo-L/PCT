# Check if a character is an operator
def isOperator(op: str) -> bool:
    return op in "+-*/"

# Return the precedence of operators
def precedence(op: str) -> int:
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 0

# Convert infix expression to postfix using stack
def InfixToPostfix(infix: str) -> str:
    postfix = []
    stack = []
    
    for symbol in infix:
        if symbol.isalnum():  # Operand
            postfix.append(symbol)
        
        elif isOperator(symbol):  # Operator
            while stack and isOperator(stack[-1]) and precedence(stack[-1]) >= precedence(symbol):
                postfix.append(stack.pop())
            stack.append(symbol)
        
        elif symbol == '(':  # Left parenthesis
            stack.append(symbol)
        
        elif symbol == ')':  # Right parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '(' from stack
    
    # Pop all remaining operators in the stack
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

# Evaluate a postfix expression using stack
def evalPostfix(postfix: str) -> int:
    stack = []
    
    for symbol in postfix:
        if symbol.isdigit():  # Operand
            stack.append(int(symbol))
        elif isOperator(symbol):  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            if symbol == '+':
                stack.append(operand1 + operand2)
            elif symbol == '-':
                stack.append(operand1 - operand2)
            elif symbol == '*':
                stack.append(operand1 * operand2)
            elif symbol == '/':
                stack.append(operand1 // operand2)  # Integer division

    return stack.pop()

# Main function to take infix input, convert to postfix, and evaluate
if __name__ == '__main__':
    infix_expr = input("수식 입력: ")
    postfix_expr = InfixToPostfix(infix_expr)
    print(f"후위 표기법 변환: {postfix_expr}")
    result = evalPostfix(postfix_expr)
    print(f"연산 결과: {result}")
