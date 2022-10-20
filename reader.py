import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt 


df = pd.read_csv("iris.csv")
print(df.head())
print(df.describe())

sb.scatterplot(
    x = "sepal.length",
    y = "sepal.width",
    data = df
)
plt.show()

print(df.corr(df['sepal.length'],df['petal.length']))
