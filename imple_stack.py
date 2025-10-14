stack=[]
max_size=5
def push(item):
    if len(stack)>=max_size:
        print('stack overflow!!',item)
    else:
        stack.append(item)
        print('pushed item is:',item)
def pop(item):
    if is_empty():
        print('underflow')
        return None
    else:
        item=stack.pop()
        print('popped item:',item)
        return item
def peek():
    if is_empty():
        print("stack is empty")
        return None
    else:
        print('top ele is:',stack[-1])
        return [-1]
def is_empty():
    return len(stack)==0
def display():
    if is_empty():
        print('stack is empty')
    else:
        print('stack ele (top --> bottom)')
        for item in reversed(stack):
            print(item)
#example usage
while True:
    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice=int(input('enter ur choice:'))
    if choice==1:
        item = int(input("Enter item to push: "))
        push(item)
    elif choice==2:
        pop(item)
    elif choice==3:
        peek()
    elif choice==4:
        display()
    else:
        if choice==5:
            print('exit program..!')
        else:
            print('enter valid choicee')

