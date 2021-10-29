def countpaths(n):
    #base cases
    if n==0: #because at 0 there exits 1 way that is stay there and don't move
        return 1
    elif n<0:
        return 0
    n1 = countpaths(n-1)
    n2 = countpaths(n-2)
    n3 = countpaths(n-3)

    cp = n1+n2+n3
    return cp
    
if __name__ == "__main__":
    n = int(input())
    print(countpaths(n))
