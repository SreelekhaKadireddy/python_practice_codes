n=int(input())
i=1
sum1=0
while (i<=n//2):
    if n%i==0:
        sum1=sum1+i
    i=i+1
if sum1==n:
    print("perfect number")
else:
    print("not")
