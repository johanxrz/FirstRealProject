import pandas as pd 

df = pd.read_csv('data.csv')

df.head()  # Display the first few rows of the dataframe

df.describe()  # Get summary statistics of the dataframe

df["value"].max()  # Calculate the max of the 'value' column
