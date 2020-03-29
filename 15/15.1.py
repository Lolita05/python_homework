import re


reg_pattern = r'/(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+/'
with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/references.txt", "r") as f1:
    with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/references2.txt", "w+") as f2:
        match = re.findall(reg_pattern, f1.read())
        f2.write('\n'.join(match))
