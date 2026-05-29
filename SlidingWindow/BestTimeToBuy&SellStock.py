prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    left = 0
    right = 0
    maxProfitDay = 0

    while right < len(prices):
        if prices[right] < prices[left]:
            left = right
        else:
            profit = prices[right] - prices[left]
            maxProfitDay = max(maxProfitDay, profit)
        right += 1
    return maxProfitDay


print(maxProfit(prices=prices))
