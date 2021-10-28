n = int(input())
a =[]
for i in range(0,n):
    a.append(int(input()))
    
for i in range (max(a),0,-1):
    for j in range (0,len(a)):
        if a[j] == i or a[j] > i:
            print("*\t", end="")
            
        else:
            print("\t", end="")
    print() #new line without white space
