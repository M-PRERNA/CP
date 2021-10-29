# count stairs memoization
def countpaths(n,count):
    #base cases
    if n==0:
        return 1
    elif n<0:
        return 0
    
    if count[n]>0:
        return count[n]
    print("hey: ",n)
    n1 = countpaths(n-1,count)
    n2 = countpaths(n-2,count)
    n3 = countpaths(n-3,count)
    cp = n1+n2+n3
    
    count[n] = cp
    
    return cp
    
if __name__ == "__main__":
    n = int(input())
    count = [0]*(n+1)
    print(countpaths(n,count))
