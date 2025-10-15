stack=[]
def push(item):
        stack.append(item)
        
def pop(item):
    if is_empty():
        print('stack underflow')
    else:
        stack.pop(item)
        
def is_empty():
    return len(stack)==0

def is_palindrome(s):
    for ch in s:
        push(ch)
    reversed_s=''
    while not is_empty():
        reversed_s += stack.pop()
    if s==reversed_s:
        print('palindrome')
    else:
        print('it is not palindrome')
s = input("Enter a string: ")
is_palindrome(s)
        
    
          
  
            


