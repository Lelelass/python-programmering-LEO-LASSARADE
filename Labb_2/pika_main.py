import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd
import pika_data as pida
import pika_calc as picalc


pikachu_data = pida.read_and_format('pikachu.csv')
pichu_data = pida.read_and_format('pichu.csv')

pikachu_training_data, pikachu_test_data = pida.sample_randomization(pikachu_data)# The function returns two dataframess as a tuple, I store each dataframe in an appropriate variable for test and train data
pichu_training_data, pichu_test_data = pida.sample_randomization(pichu_data)

test_points = pida.test_df_to_coordinates_list(pikachu_test_data, pichu_test_data)# List of the ten test points' coordinates

pikachu_classified = 0
pichu_classified = 0

for test_point in test_points : #each test point will be tested against it's 5 closest points in both datasets.
    pikachu_training_data = picalc.test_point_distance(test_point, pikachu_training_data)# Calls function for adding a column distance to dataframe
    pichu_training_data = picalc.test_point_distance(test_point, pichu_training_data)

    pikachu_distances = pida.sort_and_list(pikachu_training_data) #This sorts the dataframe with distance to point ascending, and returns a list of the 5 smallest values. (5 closest points to test value)
    pichu_distances = pida.sort_and_list(pichu_training_data)

    print(pikachu_distances)
    print(pichu_distances)


    closer_matches = {"pikachu" : [], "pichu": []}
    for distance_pika in pikachu_distances:
        do_break = False
        for distance_pichu in pichu_distances:
            if distance_pika < distance_pichu:
                continue
            else:
                if distance_pichu not in closer_matches['pichu']: #prevent double matching of the condition, and double adding to the dict.
                    closer_matches['pichu'].append(distance_pichu)
                    do_break = True
                else:
                    do_break = True
        
        if do_break != True:
            closer_matches['pikachu'].append(distance_pika)


    if len(closer_matches['pikachu']) > len(closer_matches['pichu']):
        pikachu_classified += 1
        print(f"Test point is likely a pikachu ({len(closer_matches['pikachu'])} closer pikachus, {len(closer_matches['pichu'])} closer pichus)")
    else:
        pichu_classified += 1
        print(f"Test point is likely a pichu ({len(closer_matches['pikachu'])} closer pikachus, {len(closer_matches['pichu'])} closer pichus)")

print(f"test points were classified as {pikachu_classified} pikachus and {pichu_classified} pichus. Expected 5 pikachus and 5 pichus")



    #pikachu_training_data = picalc.test_point_distance((pikachu_test_data.iloc[0][0], pikachu_test_data.iloc[0][1]), pikachu_training_data)

'''
    i = 0

    while i < 5:
        test_point = (pichu_test_data.iloc[i][0],pichu_test_data.iloc[i][1])
        pikachu_training_data = picalc.test_point_distance(test_point, pikachu_training_data)# Calls function for adding a column distance to dataframe
        pichu_training_data = picalc.test_point_distance(test_point, pichu_training_data)
        pikachu_training_data.sort_values('distance')
        pichu_training_data.sort_values('distance')
        distance_to_pikachu = pikachu_training_data['distance'].min()# Minimal value for column distance
        distance_to_pichu = pichu_training_data['distance'].min()
        if distance_to_pichu > distance_to_pikachu:
            pikachu_count += 1
        else:
            pichu_count += 1
        i += 1

    print(f"test data counted as {pikachu_count} pikachus and {pichu_count} pichus")

'''




# tittle x labels Y labels, färg + teckestil (kryss) - legend
plt.scatter(pikachu_training_data.iloc[:,0], pikachu_training_data.iloc[:,1])
plt.scatter(pichu_training_data.iloc[:,0], pichu_training_data.iloc[:,1])
plt.scatter(pichu_test_data.iloc[:,0], pichu_test_data.iloc[:,1])
plt.scatter(pikachu_test_data.iloc[:,0], pikachu_test_data.iloc[:,1])
