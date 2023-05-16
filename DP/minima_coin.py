
# top-down
def coinSearch(coin_type: list[int], amount: int):
    
    memo = {}
    def dp(amount: int):
        # base case
        if amount == 0: return 0
        if amount < 0: return -1
        if amount in memo: return memo[amount]

        res = float("inf")
        
        # check status: amount 改變
        for coin in coin_type: # check select: coin
            subProblem = dp(amount - coin)
            # no solution -> pass
            if subProblem == -1: continue
            res = min(res, subProblem+1)
            memo[amount] = res # check dp

        return memo[amount]
    
    return dp(amount)

# bottom-up
def coinSearch2(coin_type: list[int], amount: int):
    
    dp = [amount + 1 for i in range(amount+1)]
    dp[0] = 0 # base case

    for i in range(amount+1): 
        for coin in coin_type:
            if i - coin < 0: continue
            dp[i] = min(dp[i], 1+dp[i-coin]) # 此處1代表該coin

    return dp[amount] if dp[amount] != (amount+1) else -1 

    
    

if __name__ == "__main__":
    print(coinSearch([1, 5, 10], 9))
    