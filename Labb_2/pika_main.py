import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd
import pika_data as pida



pikachu_data = pida.read_and_format('pikachu.csv')
pichu_data = pida.read_and_format('pichu.csv')

print(type(pikachu_data.iloc[0][0]))

print(pikachu_data.head())
print(pichu_data.head())


# tittle x labels Y labels, färg + teckestil (kryss) - legend
plt.scatter(pikachu_data.iloc[:,0], pikachu_data.iloc[:,1])
plt.scatter(pichu_data.iloc[:,0], pichu_data.iloc[:,1])

#Eucl avståndet från testpunkt till datapunkt (varje punkt)

