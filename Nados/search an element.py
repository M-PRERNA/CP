n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
flag = False
for i in range (n):
    if a[i] == d:
        print(i)
        flag = True
if flag == False: print(-1)
