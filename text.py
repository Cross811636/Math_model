__author__ = 'pwq'
a = ['rs12036216', 'rs2477777', 'rs3128342', 'rs28603108', 'rs12133956', 'rs946758', 'rs880801', 'rs4391636', 'rs7418164', 'rs1541318', 'rs2071999', 'rs364642', 'rs7368252', 'rs7522344', 'rs12036552', 'rs277671', 'rs1009113', 'rs12070592', 'rs10864301', 'rs4908635', 'rs1193219', 'rs10864304', 'rs707472', 'rs2797682', 'rs226242', 'rs1004557', 'rs2273298', 'rs11121557', 'rs2480772', 'rs2982376', 'rs11121742', 'rs761087', 'rs4073574', 'rs4845881', 'rs10779765', 'rs17367504', 'rs198411', 'rs4845892', 'rs3013045', 'rs1148455', 'rs2038095', 'rs7543486', 'rs1569635', 'rs3765380', 'rs6429695', 'rs2473345', 'rs2092324', 'rs3766160', 'rs4646092', 'rs17383551', 'rs2143810', 'rs2244300', 'rs2134482', 'rs16830759', 'rs648305', 'rs12097284', 'rs697760', 'rs2095518', 'rs4310409', 'rs1138333', 'rs7555171', 'rs2473808', 'rs1883567', 'rs11573253', 'rs652536', 'rs10916825', 'rs212531', 'rs829404', 'rs12128325', 'rs2473246', 'rs2473253', 'rs2505722', 'rs2807345', 'rs11580218', 'rs2182703', 'rs7536195', 'rs586589', 'rs588641', 'rs4649124', 'rs4649168', 'rs10903032', 'rs17184651', 'rs1702311', 'rs12736858', 'rs932372', 'rs6699113', 'rs3820514', 'rs15045', 'rs1257163', 'rs11247865', 'rs12752833', 'rs4466676', 'rs6699701', 'rs7543405', 'rs313990', 'rs9659647', 'rs9426306', 'rs2428556', 'rs10915035', 'rs9286945', 'rs1372371', 'rs11587046', 'rs4949238', 'rs1201394', 'rs1924270', 'rs1033867', 'rs7555715', 'rs1188399', 'rs3795438', 'rs1891419', 'rs12145450']
f = open("genotype_di.dat","rb")

line = f.readline()
label = line.strip().split(" ")
def get_content(index):
    print label[index]
get_content(8379)