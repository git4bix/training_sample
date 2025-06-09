from random import randint
from collections import Counter

ran = randint(1,1000000)

ran1 = [ ran for item in range(1000000)]

print(Counter(ran1))