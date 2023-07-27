def res(n,m):
    div=0
    non_div=0
    for i in range(1,m+1):
        if i%n==0:
            div+=1
        else:
            non_div+=i
    diff=abs(non_div-div)
    return diff
m=int(input())
n=int(input())
print(res(n,m))
