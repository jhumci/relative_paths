import pandas as pd
import os


print( "Current working directory: ", os.getcwd() )

# Relative path to the file in the sample_data directory
df = pd.read_csv("../sample_data/california_housing_train.csv")

print(df.head())