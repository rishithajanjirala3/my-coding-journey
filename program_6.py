#lcm of two numbers
#method 1 using math module
import math
a,b=list(map(int,input().split()))
print(math.lcm(a,b))

#method 2 
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a,b=list(map(int,input().split()))
print(lcm(a,b))