#Займёмся парсингом рассказа в файле 2430AD! Для начала извлеките оттуда все числа

import re

no = r'[-+]?\d*\.\d+|\d+'

with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/2430AD.txt", 'r') as text:
    with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/hjm.txt", 'w+') as nums:
        line = re.findall(no, text.read())
        nums.write('\n'.join(line))