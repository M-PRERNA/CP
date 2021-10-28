n = int(input())
d = int(input())
# string conversion
s = str(n)
l = [int(i) for i in s]
print(l.count(d))
