def valid_paranthesis(s):
    stack=[]
    for ele in s:
        if ele in '[{(':
            stack.append(ele)
        else:
            if len(stack)==0:
                return False
            x=stack.pop()
            if x=='(' and ele==')' or x=='[' and ele==']'or x=='{' and ele=='}':
                continue
            else:
                return False
    return len(stack)==0
s='[({})]'
print(valid_paranthesis(s))
        


        

    