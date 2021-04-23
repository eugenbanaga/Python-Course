from random import random, randrange
from time import sleep

bananas_count = input("How many bananas:")

try:
    bananas_count = int(bananas_count)
except ValueError:
    print("Bad bananas count, applying default value of 20")
    bananas_count = 20

max_rotten_bananas = int(bananas_count * 0.2)

max_rotten_bananas_count = 0
while bananas_count:
    if 20 <= randrange(0, 100, 1) <= 50:
        print("Banana is rotten, monkey is angry")
        max_rotten_bananas_count += 1
        print("Rotten bananas count " + str(max_rotten_bananas_count))
        continue
    if max_rotten_bananas_count == max_rotten_bananas:
        print("You are heavily injured by monkey for providing too much rotten bananas")
        break
    print("Monkey is eating the banana")
    sleep(1)


