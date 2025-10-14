def rev_arr(arr):
    stack=[]
    for item in arr:
        stack.append(item)
    for i in range(len(arr)):
        arr[i]=stack.pop()
    return arr
arr=list(map(int,input().split()))
print("original arr:",arr)
print('reversed arr:',rev_arr(arr))