'''
0-1 Knapsack Implementation using Dynamic Programming

Problem:
Given weight and value of certain items with 1 quantity each and maximum weight allowed in the knapsack, 
how do we pick items such that both the sum of weight of items picked is less than or equal to maximum allowed weight and value of such items is maximized

'''

def knapsack():
    '''
    totalWeight: represents the weight units that the knapsack can hold at maximum capacity
    n: represents the total number of items in the knapsack
    value: list of values that represents each item's value
    weight: list of weights for each item
    '''
    totalWeight = 10
    n = 4
    value = [10, 40, 30, 50]
    weight = [5, 4, 6, 3]

    # matrix for memoization initialized with 0's
    # each row represents up to that item specifically (i.e. row 2 represents consideration from both item 1 and 2)
    # each column represents the total weight units in consideration with the respective items considered
    memo = [[0 for x in range(totalWeight + 1)] for x in range(n + 1)]
    
    # Run on every cell in the matrix except for the base cases
    for item in range(1, n + 1):
        for capacity in range(1, totalWeight + 1):
            '''
            maxWithoutCurrent: the previous maximum value possible, which is guaranteed to exist
            maxWithCurrent: the maximum value possible with the current value + remaining weight's value
            currentWeight: current weight of the item we're evaluating
            '''
            maxWithoutCurrent = memo[item - 1][capacity]
            maxWithCurrent = 0
            currentWeight = weight[item - 1]
            
            # check if the knapsack can even fit the current item's weight
            if capacity >= currentWeight:
                # include the previous row's value instead of the default zero
                maxWithCurrent = value[item - 1]
                # calculate the remaining weight that is remaining and add the previously calculated value into maxWithCurrent
                remainingCapacity = capacity - currentWeight
                # add previous row's value and remaining capacity's value
                maxWithCurrent += memo[item - 1][remainingCapacity]

            # choose the maximum possible value between previous row's value versus current value + remaining value
            # in other words, pick either the maximum value that we can obtain without current item, or the maximum value that we can obtain along with current item
            memo[item][capacity] = max(maxWithCurrent, maxWithoutCurrent)

    print(f"With {n} total items and a knapsack that can carry a maximum of {totalWeight} units, the maximum value possible is {memo[n][totalWeight]}.")
    
    # visual representation of the memoization matrix
    print(memo)

knapsack()