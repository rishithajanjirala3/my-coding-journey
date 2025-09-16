#sum of n natural numbers

#method 1 using loop
n=int(input('enter num:'))
sum=0
for i in range(n+1):
    sum+=1
print(sum)

#method 2 using formula
n=int(input('enter num: '))
print(n*(n+1)//2)

#method 3 using recursion
def sumOfn(n):
    if n==1:
        return 1
    return n+sumOfn(n-1)
n=int(input('enter num: '))
print(sumOfn(n))


