n=int(input())
fact=[]
i=1
while (i<n):
    if n%i==0:
        fact.append(i)
    i=i+1
if sum(fact)>n:
    print("abundant number")
else:
    print("not")
