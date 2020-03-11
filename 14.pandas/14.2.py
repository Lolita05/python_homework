import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/lolitiy/Documents/inst_bioinf_19_20/python/train.csv', sep=';') #когда вставляла ссылску на гитхаб, он ругался
df.style.hide_index()

# Nucleotide values
A = df["A"].values
C = df["C"].values
T = df["T"].values
G = df["G"].values

count_row = df.shape[0] # gives number of row count == 63
fig, ax = plt.subplots(figsize=(20, 10)) # using the variable ax for single a Axes
l_loc = np.arange(0, 2*count_row, 2) # the label locations
width = 0.5  # the width of the bars

# Nucleotide bars
ax.bar(l_loc, A, width, label="A", color = "teal")
ax.bar(l_loc+2*width, C, width, label="C", color = "indigo")
ax.bar(l_loc+4*width, T, width, label="T", color = "tomato")
ax.bar(l_loc+6*width, G, width, label="G", color = "gold")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Freq')
ax.set_xlabel('Nucleotides')
ax.set_title('Number Distribution of Nucleotide values')
ax.set_xticks(l_loc + width)
ax.set_xticklabels(df.pos.values)
ax.tick_params(axis="x", labelsize=10, labelrotation=45)
ax.legend(loc = "best")

plt.show()