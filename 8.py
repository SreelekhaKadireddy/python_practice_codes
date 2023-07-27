def res(arr,num,d):
    if d not in arr:
        return -1
    c=0
    for i in arr:
        if abs(num-i)<d:
            c+=1
    return c
    
arr=list(map(int,input().split()))
num=int(input())
d=int(input())
print(res(arr,num,d))
