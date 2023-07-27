n=int(input())
sq=pow(n,2)
t=sq%10
if n%10==t:
    print("automorphic")
else:
    print("not")
