## PLOTTING A VERTICAL BAR CHART-JIE JENN YT

import numpy as np
import matplotlib.pyplot as plt

labels =["A","B","C"]
values = [1000,2000,3000,]

plt.style.use("ggplot")

fig,ay = plt.subplots(figsize=(10,5))

#plotting  a  vertical bar chart 
ay.bar(labels,values)

plt.show()
