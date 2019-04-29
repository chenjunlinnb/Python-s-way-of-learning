import random
import time
start=time.time()
s=[]
while len(s)<10000:
    s.append(random.randint(0,10000))
stop=time.time()
print(stop-start)
