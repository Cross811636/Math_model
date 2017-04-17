# -*- coding:utf-8 -*-
num = input('第一行数据：')
num_2 = input('希望去掉的数字数量：')
comp_num=str(num)
print comp_num
for j in range(len(num_2)):
    for i in range(0, len(comp_num)):
        if comp_num[0] < comp_num[i]:
            comp_num.pop(0)
print comp_num
