#паттерн для поиска email адресов

no = r'\([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)\'
text = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/2430AD.txt", 'r')
e_mails = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/hjm.txt", 'w+')

for line in text:
    out = re.findall(no, line)
    for i in out:
        e_mails.write(i + '\n')
text.close()
e_mails.close()
