def sumi(a,n):
    for i in a:
        if n-i in a:
          return True
    return False

a=list(map(int,input().split()))
n=int(input())
print(sumi(a,n))
