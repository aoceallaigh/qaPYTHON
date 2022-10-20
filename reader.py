import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt 


df = pd.read_csv("test.csv")
print(df.head())
print(df.describe())

newplot = sb.scatterplot(
    x = "Weight",
    y = "Age",
    data = df 
)
plt.show()