n = int(input())
b = int(input())
ans = 0
p = 1
while (n>0):
    r = n%b
    n = n//b
    ans += r * p 
    p *= 10
    
print(ans)
