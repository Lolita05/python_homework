#паттерн для поиска email адресов
import re

no = r'\([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)\'

with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/2430AD.txt", 'r') as text:
    with open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/hjm.txt", 'w+') as e_mails:
        line = re.findall(no, text.read())
        e_mails.write('\n'.join(line))
