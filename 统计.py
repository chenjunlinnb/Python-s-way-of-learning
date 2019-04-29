f=open("F:\\junior\\FF\\python\\计数.txt",'r')
s=list(f.read().split(','))
print(s)
d=dict()
for i in s:
    d[i]=d.get(i,0)+1
for i in d.items():
    print(i)

