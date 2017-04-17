#-*- coding:utf-8 -*-
f=open('genotype.dat','rb')
file=open('binary.dat','wb') #怎样写入文件
n=0
line=f.readlines()

while line:
    n+=1
    line.strip().replace('A','00').replace('T','01').replace('C','10').replace('G','11')#字符串变成
    line=f.readlines()
    file.write(line)
print type(line)
print n
f.close()
