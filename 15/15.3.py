#Теперь выберите из текста все слова, в которых есть буква a, регистр при этом не важен

import re

pattern = r'\b\w*[aA]\w*\b'

with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/2430AD.txt", 'r') as text:
    with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/hjm.txt", 'w+') as lett:
        line = re.findall(pattern, text.read())
        lett.write('\n'.join(line))
