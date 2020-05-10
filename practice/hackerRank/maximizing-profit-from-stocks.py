
def maximumProfit(price):
    if len(price) <= 1:
        return 0

    profit = 0
    price_max = price[-1]
    for i in range(len(price)-1, -1, -1):
        print(price[i])
        if price_max < price[i]:
            price_max = price[i]
        else:
            profit += price_max - price[i]
    return profit
