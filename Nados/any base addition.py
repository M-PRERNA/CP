base = int(input())
n1 = int(input())
n2 = int(input())
ans=0
carry=1
p = 1
s = 0
while (n1 or n2 or carry):
    a = n1%10 
    b = n2%10
    s += a+b
    
    if (s)>(base-1):
        rem = (s)%base
        carry = (s)//base
        ans += rem*p
        p = p*10
    else:
        rem = (s)%base
        carry = (s)//base
        ans += rem*p
        p = p*10 
    n1 = n1//10
    n2 = n2//10
    s = carry
print(ans)
