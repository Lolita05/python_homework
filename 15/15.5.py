#гистограмму распределения длин уникальных слов (без учёта регистра, длина от 1) в тексте

import re
import pylab

pattern = re.compile(r'(\w+\b)(?!.*\1\b)')

text = open("/Users/lolitiy/Documents/inst_bioinf_19_20/python/2430AD.txt", 'r')
uniqueWords = pattern.findall(text.read().lower(), re.I)
uniqueWords = set(uniqueWords)
lengths = list(map(len, uniqueWords))

pylab.hist(lengths, bins=20, color='plum')
pylab.title("%i words\nLengths %i to %i" % (len(lengths), min(lengths), max(lengths)))
pylab.xlabel("Word length")
pylab.xlabel("Count")
pylab.show()
