#Сохраните в файл train_part.csv следующую часть из файла train.csv:
# строки, где matches больше чем среднее
# колонки pos, reads_all, mismatches, deletions, insertions

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/lolitiy/Documents/inst_bioinf_19_20/python/train.csv', sep=';') #когда вставляла ссылску на гитхаб, он ругался
df.style.hide_index()

train_part_df = df[["matches", "pos", "reads_all", "mismatches", "deletions", "insertions"]]
train_part_df = train_part_df[train_part_df.matches > train_part_df["matches"].mean()]

train_part_df.to_csv('/Users/lolitiy/Documents/inst_bioinf_19_20/python/"train_part.csv")