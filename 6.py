def result(string):
    if (len(string)%2==0):
        print('invalid input')
    i=1
    result=int(string[0])
    while i<len(string):
        if string[i]=='A':
            result&=int(string[i+1])
        elif string[i]=='B':
            result|=int(string[i+1])
        elif string[i]=='C':
            result^=int(string[i+1])
        i=i+2
    return result
            

a=input()
print(result(a))
