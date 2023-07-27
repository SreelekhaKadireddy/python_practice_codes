s=input()
def save(s):
    for i in s:
        if i in ['?','{','}','[',']','/','@','!',' ','&','^','<','>','$',',',':',';']:
            s=s.replace(i,'')
    a=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    for i in s:
        p=ord(i)
        if p in a:
            p=p+32
            p=chr(p)
    else:
        print('invalid')
    if s==s[::-1]:
        print('YES')
    else:
        print('NO')
        
save(s)
