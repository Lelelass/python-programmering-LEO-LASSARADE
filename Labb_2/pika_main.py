import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd
import pika_data as pida
import pika_calc as picalc


pikachu_data = pida.read_and_format('pikachu.csv')
pichu_data = pida.read_and_format('pichu.csv')

pikachu_training_data, pikachu_test_data = pida.sample_randomization(pikachu_data)# Functionen returnerar en tuple så jag vill komma åt första värden i tuplet
pichu_training_data, pichu_test_data = pida.sample_randomization(pichu_data)

test_point = (pikachu_test_data.iloc[0][0], pikachu_test_data.iloc[0][1])
print(test_point)
#((P[0]-Q[0])**2 + (P[1]-Q[1])**2)

pikachu_training_data['distance']  = ((pikachu_training_data['Width'] - test_point[0])**2 + (pikachu_training_data['Height'] - test_point[1])**2)**0.5
pichu_training_data['distance']  = ((pichu_training_data['Width'] - test_point[0])**2 + (pichu_training_data['Height'] - test_point[1])**2)**0.5

print(pikachu_training_data)
print(pichu_training_data)



# tittle x labels Y labels, färg + teckestil (kryss) - legend
plt.scatter(pikachu_training_data.iloc[:,0], pikachu_training_data.iloc[:,1])
plt.scatter(pichu_training_data.iloc[:,0], pichu_training_data.iloc[:,1])
plt.scatter(pichu_test_data.iloc[:,0], pichu_test_data.iloc[:,1])
plt.scatter(pikachu_test_data.iloc[:,0], pikachu_test_data.iloc[:,1])

#Eucl avståndet från testpunkt till datapunkt (varje punkt)

