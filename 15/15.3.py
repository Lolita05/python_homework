#Теперь выберите из текста все слова, в которых есть буква a, регистр при этом не важен

import re

no = r'\b\w*[aA]\w*\b'
text = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/2430AD.txt", 'r')
numbers_from_text = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/hjm.txt", 'w+')

for line in text:
    out = re.findall(no, line)
    for i in out:
        numbers_from_text.write(i + '\n')
text.close()
numbers_from_text.close()