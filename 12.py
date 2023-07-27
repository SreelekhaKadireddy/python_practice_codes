def sol(n,fact):
    i=1
    while(i<n):
        if n%i==0:
            fact.append(i)
        i=i+1
    return sum(fact)-n
    

n1=int(input())
n2=int(input())
fact=[]
if int(sol(n1,fact)/n1)==int(sol(n2,fact)/n2):
    print("friendly numbers")
else:
    print("not")
