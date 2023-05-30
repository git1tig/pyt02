import random
import math

num_coins = 5
coins = []
res1 = 0
res2 = 0
for i in range(num_coins):
    coins.append(random.randint(0, 1))
    if coins[i] == 0:
        res1 += 1
    else:
        res2 += 1
print(coins)
if res1 > res2:
    print(f'Что бы все лежали ровно надо {res2} перевернуть!')
else:
    print(f'Что бы все лежали ровно надо {res1} перевернуть!')
