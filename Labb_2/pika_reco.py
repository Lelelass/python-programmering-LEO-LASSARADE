import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd

def read_and_format(csv_file):
        df = pd.read_csv(csv_file)
        df.columns.values[0] = "Width"# Manuellt n¨mning av kolumner
        df.columns.values[1] = "Height"
        df.iloc[:, 0] = df.iloc[:, 0].str.replace(r'(', '', regex=True)# 2 rad kod för att erätta värden i celler med värden utan parenthes
        df.iloc[:, 1] = df.iloc[:, 1].str.replace(r')', '', regex=True)
        df['Width'] = df['Width'].astype(float)# 2 rad kod för att byta strings som finns i varje kolumn (original datatyp) till float
        df['Height'] = df['Height'].astype(float)
        return df


pikachu_data = read_and_format('pikachu.csv')
pichu_data = read_and_format('pichu.csv')

print(type(pikachu_data.iloc[0][0]))

print(pikachu_data.head())
print(pichu_data.head())


# tittle x labels Y labels, färg + teckestil (kryss) - legend
plt.scatter(pikachu_data.iloc[:,0], pikachu_data.iloc[:,1])
plt.scatter(pichu_data.iloc[:,0], pichu_data.iloc[:,1])

#Eucl avståndet från testpunkt till datapunkt (varje punkt)

