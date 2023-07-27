
t=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sum1=0
max1=sum1
for i in range(t):
   sum=sum+a[i]-b[i]
   if max1<sum1:
         max1=sum1
print(max1)
    
