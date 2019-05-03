dict1={
"磷离子":"12345678901",
"宋耀军":"12345678902",
"晚上":"12345678903",
"放寒假":"12345678904",
"啥客户":"12345678905",
"恢复健康":"12345678906",
"牛头":"12345678907",
"二胺":"12345678908",
"二珂":"12345678909",
"王志":"12345678910",
"帅陈":"12345678911"
}
while True:
    i=int(input("请输入：（1：表示查询，2:添加,3:删除）："))
    
    if i==1:
        name=input("请输入查询名字:")
        if dict1.__contains__(name):
            print(dict1[name])
        else:
            print("输入错误！")
        
    elif i==2:
        name=input("请输入添加的名字:")
        key=input("请输入添加的号码:")
        dict1[name]=key
    elif i==3:
        name=input("请输入删除的名字:")
        if dict1.__contains__(name):
            del dict1[name]
        else:
            print("输入错误！")
        
    else :
        print("输入错误！")
    
    key=input("是否继续:")
    if key!="n":
        print("contiune!" )
    else :
        print("继续")
        break
        
