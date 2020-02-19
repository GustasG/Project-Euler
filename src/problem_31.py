

#Source: https://www.geeksforgeeks.org/coin-change-dp-7/

def coinSums(coins, size, target_value):
    if target_value == 0:
        return 1

    if target_value < 0:
        return 0

    if size <= 0 and target_value >= 1:
        return 0

    return coinSums(coins, size - 1, target_value) + coinSums(coins, size, target_value - coins[size - 1])


coins = [1, 2, 5, 10, 20, 50, 1 * 100, 2 * 100]
value = 200

print(coinSums(coins, len(coins), value))