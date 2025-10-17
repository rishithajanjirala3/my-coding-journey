def post_fix(expression):
    stack=[]
    for ch in expression:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            one=stack.pop()
            two=stack.pop()
            if ch == '*':
                stack.append(two * one)
            elif ch == '-':
                stack.append(two - one)
            elif ch == '+':
                stack.append(two + one)
            elif ch == '/':
                stack.append(two / one)
            elif ch == '^':
                stack.append(two ** one)
    return stack.pop()

expression = input("Enter postfix expression: ")
print("Result:",post_fix(expression))


