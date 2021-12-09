def coinChange(coins, amount):
    maxg = amount + 1    
    dp = [maxg] * (amount + 1) # because each coin atleast needs to be 1 rupee, 
    # if we use 1 rupee coins, then min possible change will be equal to amount
    # if there are other coins, min possible coins will be in the range of smallest coin to largest coin
    dp[0] = 0
    for curr_amount in range(1, amount + 1):
        for coin in coins:
            # coin needs to smaller than curr_amount 5 coin and with amount 2 is not possible
            if coin <= curr_amount:
                # with current amount what is the minimum number of coins I need to use
                dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1) 
    if dp[amount] > amount: # otherwise equal to maxg is the meaning
        # if the coins are not sufficient we cannot reach dp[amount]
        return -1
    else:
        return dp[amount]

from collections import deque
def coinChangeBfs(coins, amount):
    if not amount :
        return 0
    qu = deque([(0, 0)])
    visited = [False] * (amount + 1)
    visited[0] = True
    while qu:
        totalCoins, curval = qu.popleft()
        totalCoins += 1 
        for coin in coins:
            required = curval + coin
            if required == amount:
                return totalCoins
            if required < amount:
                if not visited[required]:
                    visited[required] = True
                    qu.append((totalCoins, required))
    return - 1
            
    
                

