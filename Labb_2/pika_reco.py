import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd

def read_and_format(csv_file):
        df = pd.read_csv(csv_file)
        df.columns.values[0] = "Width"
        df.columns.values[1] = "Height"
        df.iloc[:, 0] = df.iloc[:, 0].str.replace('(', '')
        df.iloc[:, 1] = df.iloc[:, 1].str.replace(')', '')
        df['Width'] = df['Width'].astype(float)
        df['Height'] = df['Height'].astype(float)
        return df


pikachu_data = read_and_format('pikachu.csv')
pichu_data = read_and_format('pichu.csv')

print(type(pikachu_data.iloc[0][0]))

print(pikachu_data.head())
print(pichu_data.head())



plt.scatter(pikachu_data.iloc[:,0], pikachu_data.iloc[:,1])
plt.scatter(pichu_data.iloc[:,0], pichu_data.iloc[:,1])
