def result(a):
    dup=[]
    real=[]
    for i in range(len(a)):
        if a[i]=='#':
            dup.extend(a[i])
        else:
            real.extend(a[i])
    a=dup+real
    return a
            
a=input()
p=result(a)
for i in range(len(p)):
    print(p[i],end='')
