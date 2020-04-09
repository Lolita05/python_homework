#извлеките все восклицательные предложения

import re

pattern = r''

with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/2430AD.txt", 'r') as text:
    with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/hjm.txt", 'w+') as sentenceExclamationPoint:
        line = re.findall(pattern, text.read())
        sentenceExclamationPoint.write('\n'.join(line))
