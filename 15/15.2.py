#Займёмся парсингом рассказа в файле 2430AD! Для начала извлеките оттуда все числа

import re

no = r'(0|[1-9][0-9]*)'
text = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/2430AD.txt", 'r')
numbers_from_text = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/hjm.txt", 'w+')

for line in text:
    out = re.findall(no, line)
    for i in out:
        numbers_from_text.write(i + '\n')
text.close()
numbers_from_text.close()