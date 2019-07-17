'''
Coin Change Problem Implementation using Dynamic Programming (Bottom-Up Approach)

Problem:
Given coins of certain denominations with unlimited quantity and a total, 
what is the minimum number of coins would be needed to form that total. 


Time complexity:
Space complexity:

'''

def coinchange():
    # given list of coins of certain denominations and a target total value to reach
    coins = [1, 2, 5]
    targetAmount = 11

    # list for memoization initialized with a placeholder value (targetAmount + 1) that will be replaced by a minimum value later
    # base case also added in the front of the list to satisfy the base case of value 0
    # each index in memoization list represents the minimum number of coins for that respective index and target value, i.e. index 3 represents targetAmount = 3
    memo = [targetAmount + 1 for x in range(targetAmount)]
    memo.insert(0, 0)

    # bottom-up approach
    # for each index, find the minimum amount of coins to create the targetAmount with each coin in the coins list
    for amount in range(1, targetAmount + 1):
        for currentCoin in coins:
            # check if current amount can even possible be created with the current coin being compared with
            if currentCoin <= amount:
                '''
                currentValue: the current value in our memoization list
                currentCoinWithPrev: the current coin (1, 2, or 5) along with the remaining and previous subsolution that has already been calculated

                For example, if the targetAmount is 8, then currentValue would be 12 (targetAmount + 1). If the current coin, in
                consideration, is 5, then 8 - 5 = 3 and 3 has already been calculated and so we will check the 'memo' list for the previous solution to 
                create 3. We would then take this previous solution and simply add 1 to it (since its previous solution along with the coin = 5).
                '''

                currentValue = memo[amount]
                currentCoinWithPrev = memo[amount - currentCoin] + 1
                # take the minimum of the current existing value in 'memo' or the current coin along with the remaining/previous subsolution
                memo[amount] = min(currentValue, currentCoinWithPrev)

    # visual representation of the memoization matrix
    print(memo)

    print(f"The minimum number of coins that would be needed to make {targetAmount} is {memo[targetAmount]} coins.")
    return memo[targetAmount]

coinchange()