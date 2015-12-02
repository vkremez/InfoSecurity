# coding: utf-8
# iPython Demo

get_ipython().magic(u'pylab inline')

import pandas as pd
from pandas.io.data import DataReader
import matplotlib.pyplot as plt

df = DataReader("TSLA", "yahoo", " 20141130", "20151201")
df.head()

plt.plot(df.index, df['Close'])
plt.show()
