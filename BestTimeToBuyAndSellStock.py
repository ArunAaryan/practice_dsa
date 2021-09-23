def bestTimeToBuyAndSell(prices):
    buy, sell = 0, 1
    max_profit = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            max_profit = max(max_profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1
    return max_profit
res = bestTimeToBuyAndSell([7,6,4,3,1])
print(res)
