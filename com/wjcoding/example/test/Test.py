num = [1,2,3,4,5,-1,-2,-3,-4,-5]
for i in range(len(num)):
    znum = num[i]
    if znum >=0:
        print('正数：'+ str(znum))
    else:
        print('负数：'+ str(znum))

z = []
f = []
shuzu = [0,1,2,3,4,5,6,-1,-2,-3,-4,-5,-6-7]
for i in range(len(shuzu)):
    shuzua = shuzu[i]
    if shuzua >=0:
        z.append(shuzua)
    else:
        f.append(shuzua)
print('正数是：'+str(z))
print('负数是：'+str(f))

#不重复的三位数
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i+j*10+k*100)
                count += 1
print("一共有%d个三位数" % count)
