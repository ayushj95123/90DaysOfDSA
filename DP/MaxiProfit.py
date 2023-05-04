def maximumProfit(prices):
    maxi = float("-inf")
    maxiPro = float("-inf")

    for price in reversed(prices):
        maxi = max(maxi, price)
        
        diff = maxi-price
        maxiPro = max(maxiPro, diff)
        
    return maxiPro