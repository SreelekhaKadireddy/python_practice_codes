def fun(a):
    b=[]
    for i in a:
        s=a.count(i)
        b.append(i)
        if i in b:
           continue
        else:
            print(i,"occured",s,"times")
    return 1
a=[1,3,6,1,3,8,2,6,9,0,1,4,7,8]
fun(a)
        
