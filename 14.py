n=int(input())
t=n
s=[]
while (t!=0):
    s.append(t%10)
    t=t//10
if n%sum(s)==0:
    print("harshad number")
else:
    print("not")
