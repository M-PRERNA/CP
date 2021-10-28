a = [3,1,0,7,5]
b = [1,1,1,1,1,1]
arr =[]
i = len(a)-1
j = len(b)-1
carry = 0
rem = 0
ans = 0
p =1
f1 = False
f2 = False
while (i>-1 or j>-1 or carry):
    if i==-1 or j==-1:
#         f1 = True
        break
#     if j==-1:
#         f2 = True
#         break
    print(i)
    print(j)
    s = a[i]+b[j]+carry
        
    if s>9:
        ans += rem*p
        rem = s%10
        carry = s//10
        
        arr.append(s)
    else:
        ans+= (s*p)
        arr.append(s)
        
    p *= 10
    i-=1
    j-=1
print(j)
if i ==-1:
    while(j):
        print(b[j])
        j-=1
if j==-1:
    while(i):
        print(a[i])
        i-=1
# print(ans)
print("----")
for e in range (len(arr)-1,-1,-1):
    print(arr[e])
