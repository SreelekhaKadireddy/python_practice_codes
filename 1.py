s=input()
s=list(s)
p=[]
for i in range(len(s)):
    a=s[i]
    c=str(s.count(s[i]))
    if c==1:
          p.append(a)
    else:
        p.append(a)
        p.append(c)
    if int(c)>1:
        s.remove(s[i])
print(''.join(p))
