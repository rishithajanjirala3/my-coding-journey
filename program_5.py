#greatest of three numbers

#method 1 using bulit in funtion
a,b,c=list(map(int,input().split()))
print(max(a,b,c))

#nethod 2 using if-else statements
a,b,c=list(map(int,input().split()))
if a>=b and a>=c:
    print(a)
elif b>=c and b>=a:
    print(b)
else:
    print(c)