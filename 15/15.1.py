import re
f1 = open("/Users/lolitiy/Desktop/references.txt", 'r')
f2 = open("/Users/lolitiy/Desktop/references2.txt", "a")

fr = f1.readlines()
reg_pattern = re.compile('/(?:ftp.sra.ebi(?:[a-zA-Z]|[0-9]|[/_.#]|)+)/')

for line in fr:
    match = re.findall(reg_pattern, line)
    if match:
        f2.write()
f2.close()
f1.close()
