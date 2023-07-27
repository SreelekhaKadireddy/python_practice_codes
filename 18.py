def fact(temp):
    if temp==1:
        return 1
    else:
        return temp*fact(temp-1) 
n=int(input())
f=[]
while (n!=0):
    temp=n%10
    f.append(fact(temp))
    n=n//10
if sum(f)==n:
    print("strong number")
else:
    print("not")

