# -*- coding:utf-8 -*-
__author__ = 'pwq'
def get_data():
    data_set=[]
    f = open("genotype_di.dat","rb")
    f_label = open("phenotype.txt","rb")
    line = f.readline()
    label = line.strip().split(" ")
    while (line):
        tmp_list=[]
        line = f.readline()
        for i in line.strip().split(" "):
            tmp_list.append(i)
        tmp_list.append(f_label.readline().strip())
        data_set.append(tmp_list)
    print len(data_set)
    return data_set[0:1000],label
data_set,label = get_data()
numFeatures = len(data_set[0]) - 1
print numFeatures
result=[]
result_index=[]
for i in range(numFeatures):
    featList = [example[i] for example in data_set]
    throw_dict={}
    count=1
    for n in featList:
        if throw_dict.has_key(n):
            if count<=500:
                throw_dict[n]['0']+=1
            else:
                throw_dict[n]['1']+=1
        else:
            throw_dict[n] = {'0':1,'1':0}
        count+=1
    for key in throw_dict.keys():
        tmp = abs(throw_dict[key]['1']-throw_dict[key]['0'])
        if tmp>30:
            result_index.append(i)
            break

    print u"位点索引：",i
    print u'w微名称    %s'% label[i]
    print u"对应的编码信息数量分布情况：",throw_dict
    result.append(throw_dict)
print u"阈值为：",30
print u"剩余特征值的索引：",result_index
print u"剩余特征值的个数：",len(result_index)
print [label[n] for n in result_index]




