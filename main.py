import pandas as pd
import os
import seaborn as sns

print( "Current working directory: ", os.getcwd() )

# Relative path to the file
df = pd.read_csv("sample_data/california_housing_train.csv")

print(df.head())

# Plot the data and save it to a file
import matplotlib.pyplot as plt

sns.pairplot(df)
plt.savefig("pairplot.png")
