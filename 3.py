s1=input()
s2=input()
def isrotate(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        temp=s1+s1
        if s2 in s1:
            return True
        else:
            return False
print(isrotate(s1,s2))
