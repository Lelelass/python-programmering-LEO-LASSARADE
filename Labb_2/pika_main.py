import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd
import pika_data as pida
import pika_calc as picalc
import re

'''
The function read_and_format cleans the csv file (previously created by txt_to_csv.py) from parenthesis,
transforms it's values to float and store them in a dataframe with Height and Width columns
'''
pikachu_data = pida.read_and_format('pikachu.csv')
pichu_data = pida.read_and_format('pichu.csv')

'''
The function sample_randomization shuffles the index of the imported dataframes so the data is randomized.
it then slices the data in proportion 95 - 5 and returns two dataframes as a tuple.
I store each dataframe in an appropriate variable for test and for train data.
'''
pikachu_training_data, pikachu_test_data = pida.sample_randomization(pikachu_data)
pichu_training_data, pichu_test_data = pida.sample_randomization(pichu_data)

'''
Here starts the part of the exercice where a single test point is provided by an user
'''

try:
    user_input = input("Enter a width and an eight, with a blank space inbetween").split(" ")
    if not len(user_input) == 2:
            raise ValueError("You just gave one value or entered an incorrect format (or too many values)")
    for input in user_input:
        if bool(re.match('[-]', input)) == True:
            raise ValueError("No negative points please")


    user_input_point = [float(input) for input in user_input]
    #The following series of methods will be detailed in the second part of the exercice
    pikachu_training_data = picalc.test_point_distance(user_input_point, pikachu_training_data)
    pichu_training_data = picalc.test_point_distance(user_input_point, pichu_training_data)
    pikachu_distances = pida.sort_and_list(pikachu_training_data)
    pichu_distances = pida.sort_and_list(pichu_training_data)
    closer_matches = picalc.list_comparison(pikachu_distances,pichu_distances)

    if len(closer_matches['pikachu']) > len(closer_matches['pichu']):
        print(f"Your input : {user_input_point} was classified as a pikachu ({len(closer_matches['pikachu'])} closer pikachus, {len(closer_matches['pichu'])} closer pichus)")
    else:
        print(f"Your input : {user_input_point} was classified as a pichu ({len(closer_matches['pikachu'])} closer pikachus, {len(closer_matches['pichu'])} closer pichus)")
    
except ValueError as err:
    print(err)

plt.scatter(pikachu_training_data.iloc[:,0], pikachu_training_data.iloc[:,1])
plt.scatter(pichu_training_data.iloc[:,0], pichu_training_data.iloc[:,1])
plt.scatter(pichu_test_data.iloc[:,0], pichu_test_data.iloc[:,1])
plt.scatter(pikachu_test_data.iloc[:,0], pikachu_test_data.iloc[:,1])
# tittle x labels Y labels, färg + teckestil (kryss) - legend — Plot user given point ?

'''
List of the ten test points' coordinates, generated through function passed on test data. (5 from pichu file and 5 from pikachu file).
Those are the points that will be tested in the following loop
'''

test_points = pida.test_df_to_coordinates_list(pikachu_test_data, pichu_test_data)

pikachu_classified = 0 #initialising values for how points are classified by following algorithm
pichu_classified = 0

for test_point in test_points : #each test point will be tested against it's 5 closest points in both datasets.
    pikachu_training_data = picalc.test_point_distance(test_point, pikachu_training_data)# Calls function for adding a column distance to dataframe
    pichu_training_data = picalc.test_point_distance(test_point, pichu_training_data)
    pikachu_distances = pida.sort_and_list(pikachu_training_data) #This sorts the dataframe with distance to point ascending, and returns a list of the 5 smallest values. (5 closest points to test value)
    pichu_distances = pida.sort_and_list(pichu_training_data)

    print(pikachu_distances)
    print(pichu_distances)
    closer_matches = picalc.list_comparison(pikachu_distances,pichu_distances) # This as been the hardet of the exercice, comparing two lists, and extracting the minimal values to a correctly labelled dictionnary.


    if len(closer_matches['pikachu']) > len(closer_matches['pichu']):
        pikachu_classified += 1 #As the code is ran 10 times, I wanted to store all the outputs.
        print(f"Test point {test_point} classified as a pikachu ({len(closer_matches['pikachu'])} closer pikachus, {len(closer_matches['pichu'])} closer pichus)")
    else:
        pichu_classified += 1
        print(f"Test point {test_point} classified as a pichu ({len(closer_matches['pikachu'])} closer pikachus, {len(closer_matches['pichu'])} closer pichus)")

print(f"test points were classified as {pikachu_classified} pikachus and {pichu_classified} pichus. Expected 5 pikachus and 5 pichus")


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

