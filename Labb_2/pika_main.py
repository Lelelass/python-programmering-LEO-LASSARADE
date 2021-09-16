import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd
import pika_data as pida
import pika_calc as picalc


pikachu_data = pida.read_and_format('pikachu.csv')
pichu_data = pida.read_and_format('pichu.csv')

pikachu_training_data, pikachu_test_data = pida.sample_randomization(pikachu_data)# Functionen returnerar en tuple så jag vill komma åt första värden i tuplet
pichu_training_data, pichu_test_data = pida.sample_randomization(pichu_data)

#pikachu_training_data = picalc.test_point_distance((pikachu_test_data.iloc[0][0], pikachu_test_data.iloc[0][1]), pikachu_training_data)
#print(pikachu_training_data)

#test_point = (pikachu_test_data.iloc[0][0], pikachu_test_data.iloc[0][1])
#print(test_point)

#pikachu_training_data['distance']  = ((pikachu_training_data['Width'] - test_point[0])**2 + (pikachu_training_data['Height'] - test_point[1])**2)**0.5
#pichu_training_data['distance']  = ((pichu_training_data['Width'] - test_point[0])**2 + (pichu_training_data['Height'] - test_point[1])**2)**0.5
#distance_to_pikachu = pikachu_training_data['distance'].min()# Minimal value for column distance
#distance_to_pichu = pichu_training_data['distance'].min()

#print(distance_to_pikachu)
#print(distance_to_pichu)



while True:
    try:
        user_input = input("Two points separated by a space").split(" ")
        user_point = [float(value) for value in user_input]
        pikachu_traing_data = picalc.test_point_distance(user_point, pikachu_training_data)# Calls function for adding a column distance to dataframe
        pichu_traing_data = picalc.test_point_distance(user_point, pichu_training_data)
        distance_to_pikachu = pikachu_training_data['distance'].min()# Minimal value for column distance
        distance_to_pichu = pichu_training_data['distance'].min()
        if distance_to_pichu > distance_to_pikachu:
            print("it's certainly a pikachu")
        else:
            print("It's certainly a pichu")
        break
    except ValueError as err:
        print(err)
    except TypeError as err:
        print(err)


'''

i = 0
pikachu_count = 0
pichu_count = 0

while i < 5:
    test_point = (pichu_test_data.iloc[i][0],pichu_test_data.iloc[i][1])
    pikachu_training_data['distance']  = ((pikachu_training_data['Width'] - test_point[0])**2 + (pikachu_training_data['Height'] - test_point[1])**2)**0.5
    pichu_training_data['distance']  = ((pichu_training_data['Width'] - test_point[0])**2 + (pichu_training_data['Height'] - test_point[1])**2)**0.5
    distance_to_pikachu = pikachu_training_data['distance'].min()# Minimal value for column distance
    distance_to_pichu = pichu_training_data['distance'].min()
    if distance_to_pichu > distance_to_pikachu:
        pikachu_count += 1
    else:
        pichu_count += 1
    i += 1

print(f"test data counted as {pikachu_count} pikachus and {pichu_count} pichus")




# tittle x labels Y labels, färg + teckestil (kryss) - legend
plt.scatter(pikachu_training_data.iloc[:,0], pikachu_training_data.iloc[:,1])
plt.scatter(pichu_training_data.iloc[:,0], pichu_training_data.iloc[:,1])
plt.scatter(pichu_test_data.iloc[:,0], pichu_test_data.iloc[:,1])
plt.scatter(pikachu_test_data.iloc[:,0], pikachu_test_data.iloc[:,1])

'''
