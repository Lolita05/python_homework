#Нарисуем свой любимый график

import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()


data = np.random.rand(10, 12)
sns.heatmap(df.corr(), annot = True, linewidth = 0.5)
