import  pandas as pd
import numpy as np
import seaborn
from matplotlib import pyplot as plt


data = pd.read_csv("sss.CSV")

seaborn.lineplot(x=data['year'],y=np.log(data['jp']))
seaborn.lineplot(x=data['year'],y=np.log(data['us']))
plt.show()

