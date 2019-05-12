list1=["暴力","黄色","草","傻","日","干","哼","卿卿","我","拿","打","屁"]
f=open(r'F:\junior\FF\python\热词.txt','r')
f=f.read()
for i in list1:
    if(f.find(i)):
        f=f.replace(i,"**")
print(f)
        
