n=int(input())
for i in range(n+1):
    for j in range(n+1):
        if j<n-1:
            print("",end='')
        else:
            print("*",end='')
    print("\r")
    
    
