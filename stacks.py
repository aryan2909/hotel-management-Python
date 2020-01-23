a=[]
while True:
    b=int(input('enter your choice: 1.push 2.pop'))
    if b==1:
        x=int(input('enter value for push:'))
        a.append(x)
        print(a)

    elif len(a)==0:
        print('list is empty')
    elif b== 2:
        a.pop()
        print(a)
