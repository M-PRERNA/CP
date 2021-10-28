n = int(input())
a = []
for i in range (0,n):
    a.append(int(input()))
    
mx = a[0]
mn = a[0]

for i in range (1,n):
    if a[i]>mx:
        mx = a[i]
    if a[i]<mn:
        mn = a[i]
print(mx - mn)
