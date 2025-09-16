#greatest of 2 numbers
#method 1 using if else
a,b=list(map(int,input().split()))
if a==b:
    print('equal')
elif a>b:
    print(a)
else:
    print(b)

#method 2 use terneray operation
#method 3 use built-in function