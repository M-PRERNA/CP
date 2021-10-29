# Fibonacci DP
def fb(n,arr):
    if (n==1 or n==0):
        return n
#     if already exists in the arr then return and dont recur
    if not arr[n]==0:
        return arr[n]

    f1 = fb(n-1,arr)
    f2 = fb(n-2,arr)
    fib = f1+f2
    
    arr[n] = fib
    
    return fib
    
if __name__ == "__main__":
    n = int(input())
    arr = [0]*(n+1)
    ans = fb(n,arr)
    print(ans)
