#check whether a number is positive or negative

#method 1 using if else
num=int(input('enter num: '))

if num>=0:
    print("positive")
else:
    print("negative")

#method 2 using ternary operator

# Ternary Operator Syntax
# ( Condition ) ? ( if True : Action) : ( if False : Action) ;

num=int(input('enter num: '))

print('positvie' if num>=0 else 'negative')
