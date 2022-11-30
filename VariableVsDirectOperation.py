import time
import numpy as np
mains = time.time()
for tm in range(20):
    start = time.time()
    l = []
    for i in range(5000):
        a = i % 5
        b = a + 2
        c = a + 3
        d = float(a + 10)
    l.append(time.time() - start)
print(np.mean(l))

print("****************")

for tm in range(20):
    start2 = time.time()
    z = []
    for x in range(5000):
        b = (i % 5) + 2
        c = (i % 5) + 3
        d = float((i % 5) % 10)
    z.append(time.time()-start2)
print(np.mean(z))
print("********************************")
print(f'DIFFERENCE: {np.mean(z) - np.mean(l)}')


for tm in range(20):
    start3 = time.time()
    g = []
    for x in range(5000):
        a = int(41.4)
        b = a + x
    g.append(time.time()-start3)

for tm in range(20):
    start4 = time.time()
    u = []
    for y in range(5650): # 650 more operations than using a variable!
        b = int(41.4) + y
    u.append(time.time()-start4)
print("************")
print(f'  ONE FUNC DIFF: | {np.mean(g) - np.mean(u)})')
print("------------------")


print(f'Runtime for all: {time.time()-mains} s')





