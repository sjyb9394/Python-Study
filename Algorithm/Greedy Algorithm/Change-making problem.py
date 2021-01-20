#The change-making problem is the problem of representing a given amount of money with the fewest number of coins possible from a given set of coin denominations. 
#For the so-called canonical coin systems, like those used in the US and many other countries, a greedy algorithm of picking the largest denomination of coin which is 
#not greater than the remaining amount to be made will produce the optimal result.[5] This is not the case for arbitrary coin systems, though. 
#For instance, if the coin denominations were 1, 3 and 4, then to make 6, the greedy algorithm would choose three coins (4,1,1) whereas the optimal solution is two coins (3,3).

#Code
n = 1260
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
  count+=n//coin
  n%= coin

print(count)
