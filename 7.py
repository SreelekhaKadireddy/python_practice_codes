def res(a):
    c=0
    s=0
    d=0
    if len(a)<4:
        return 0
    if (a[0]>'0' and a[0]<'9'):
        return 0
    for i in a:
        if (i=='/' or i==' '):
            return 0
        elif(i>'0' and i<'9'):
            d+=1
        elif(i>'a' and i<'z'):
            s+=1
        elif(i>'A' and i<'Z'):
            c+=1
    if (c>0 and s>0 and d>0):
        return 1
    else:
        return 0
a=input()
print(res(a))
