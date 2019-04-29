import random
import time
start=time.time()
s=[]
while len(s)<10000:
    s1=[random.randint(0,10000)]
    s=s+s1
stop=time.time()
print(stop-start)
