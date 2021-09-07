import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd

def read_and_format(csv_file):
        df = pd.read_csv(csv_file)
        df.columns.values[0] = df.columns.values[0][1:]
        df.columns.values[1] = df.columns.values[1][:-1]
        df.iloc[:, 0] = df.iloc[:, 0].str.replace('(', '')
        df.iloc[:, 1] = df.iloc[:, 1].str.replace(')', '')
        return df


pikachu_data = read_and_format('pikachu.csv')
pichu_data = read_and_format('pichu.csv')

print(pikachu_data.head())
print(pichu_data.head())



plt.scatter(pika_data.iloc[:,0], pika_data.iloc[:,1])
plt.scatter(pichu_data.iloc[:,0], pichu_data.iloc[:,1])
