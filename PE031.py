def coinsways():
    coins = [1, 2, 5, 10, 20, 50, 100, 200] #used coins
    total = 200 #total value
    ways = [0]*(total+1) #creates list of 201 zeroes
    ways[0] = 1 # first value on list is 1
    for i in range(len(coins)): #loops tru indexes of coins 
        for j in range(coins[i], total+1):#loops tru indexes of values in ways list
            ways[j] += ways[j - coins[i]] # calculates number of ways with current indexed coin 
    return ways[-1]#returns result

print (coinsways())