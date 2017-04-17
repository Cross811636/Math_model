__author__ = 'pwq'
weidian  = raw_input("weidian ")
f = open("genotype_di.dat","rb")
line = f.readline()
line_list = line.split(" ")
index = line_list.index(weidian)
print index
item_list=[]
while (line):
    line = f.readline().split(" ")
    if len(line)>21:
        item_list.append(line[index])
    else:
        line=""
print item_list
print set(item_list)
while True:
    num = input("dd")
    print item_list[num]