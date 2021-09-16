import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd
import pika_data as pida


pikachu_data = pida.read_and_format('pikachu.csv')
pichu_data = pida.read_and_format('pichu.csv')

pikachu_training_data, pikachu_test_data = pida.sample_randomization(pikachu_data)# Functionen returnerar en tuple så jag vill komma åt första värden i tuplet

print(pikachu_training_data)
print(pikachu_test_data)

print(pikachu_data.head())
print(pichu_data.head())


# tittle x labels Y labels, färg + teckestil (kryss) - legend
plt.scatter(pikachu_data.iloc[:,0], pikachu_data.iloc[:,1])
plt.scatter(pichu_data.iloc[:,0], pichu_data.iloc[:,1])

#Eucl avståndet från testpunkt till datapunkt (varje punkt)

