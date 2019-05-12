list1=["nihao","wo","xi","huan","wo","bu","shi"]
d={}
d1={}
for i in list1:
    d[i]=d.get(i,0)+1
d1=sorted(d.items(),key = lambda x:x[1])
print(d1 )

 
