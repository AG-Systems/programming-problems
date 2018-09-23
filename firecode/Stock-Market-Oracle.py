def max_profit(prices):
    profit = 0
    for price in range(1, len(prices)):
        if prices[price] - prices[price-1] > 0:
            profit += prices[price] - prices[price-1]
    return profit
