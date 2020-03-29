import re


f1 = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/references.txt", 'r')
f2 = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/references2.txt", "w+")

reg_pattern = r'/(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+/'

for line in f1:
    match = re.findall(reg_pattern, line)
    for i in match:
        f2.write(i + '\n')
f2.close()
f1.close()
