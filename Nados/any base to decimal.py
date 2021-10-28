n = int(input())
b = int(input())
ans = 0
p = 1 
while (n>0):
    r = n%10
    ans += r*p
    n = n//10
    p = p*b

print(ans)
