#извлеките все восклицательные предложения

import re

pattern = r''
text = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/2430AD.txt", 'r')
sentenceExclamationPoint = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/hjm.txt", 'w+')

for line in text:
    out = re.findall(pattern, line)
    for i in out:
        sentenceExclamationPoint.write(i + '\n')
text.close()
sentenceExclamationPoint.close()