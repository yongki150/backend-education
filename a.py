from itertools import cycle
from time import time
s = time()
a = [1,2,3,4,5]
for i, v in enumerate(cycle(a)):
    if i == 30:  # 3.11~3.12
        break
    print(i, v)
    a[0] = 50000

print(time() - s)