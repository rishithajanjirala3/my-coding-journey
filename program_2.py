#check whether the number is even or odd

#method 1 brute force/if else
num=int(input('enter num: '))
if num%2==0:
    print('even')
else:
    print('odd')

#method 2 using ternary operator

# Ternary Operator Syntax
# ( Condition ) ? ( if True : Action) : ( if False : Action) ;

num=int(input('enter num: '))
print('even' if num%2==0 else 'odd')