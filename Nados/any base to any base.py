n = int(input())
b1 = int(input())
b2 = int(input())

a = 0
p = 1
# anybase to decimal
while(n>0):
    r = n%10
    a += r*p
    n = n//10
    p = p*b1
ans = 0   
pw = 1
# decimal to anyother base 
while(a>0):
    rem = a%b2
    ans += rem*pw
    a = a//b2
    pw = pw*10

print(ans)
