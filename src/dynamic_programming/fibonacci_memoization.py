memo = {0:0, 1:1}

def fib_memo(n,memo):
    # if n<=1:
    #     return n
    # if n==2:
    #     return 1
    # return 
    if n in memo:
        return memo[n]
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2,memo)
    return memo[n]