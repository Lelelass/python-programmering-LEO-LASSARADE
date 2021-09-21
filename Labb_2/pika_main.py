import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd
import pika_data as pida
import pika_calc as picalc
import re


pikachu_data = pida.read_and_format('pikachu.csv')
pichu_data = pida.read_and_format('pichu.csv')

pikachu_training_data, pikachu_test_data = pida.sample_randomization(pikachu_data)#I store each dataframe in an appropriate variable for test and for train data.
pichu_training_data, pichu_test_data = pida.sample_randomization(pichu_data)


# Here starts the part of the exercice where a single test point is provided by an user

try:
    user_input = input("Enter a width and an eight, with a blank space inbetween").split(" ")
    if not len(user_input) == 2: # This controls if the list has two values as expected
            raise ValueError("You just gave one value or entered an incorrect format (or too many values)")
    for input in user_input:
        if bool(re.match('[-]', input)) == True: #This prevents any minus signs to be given to a point
            raise ValueError("No negative points please")

    user_input_point = [float(input) for input in user_input] # As the calculations runned by some of the program's functions will only work on floats.
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


"""
Setup for all the matplotlib visualisation.
First shuffled dataset visualised with the user-given test point.
"""
plt.title("Visualisation of all points found in datasets")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.plot(user_input_point[0],user_input_point[1],'r+', markersize = 15, label = "User given point") 
plt.scatter(pikachu_training_data.iloc[:,0], pikachu_training_data.iloc[:,1], marker='s', label ="Pikachu training data")
plt.scatter(pichu_training_data.iloc[:,0], pichu_training_data.iloc[:,1], marker = '^', label ="Pichu training data")
plt.scatter(pichu_test_data.iloc[:,0], pichu_test_data.iloc[:,1], label ="Pichu test data")
plt.scatter(pikachu_test_data.iloc[:,0], pikachu_test_data.iloc[:,1], label ="Pikachu test data")
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')


'''
List of the ten test points' coordinates, generated through function passed on test data. (5 from pichu file and 5 from pikachu file).
Those are the points that will be tested in the following loop, as the program now will compare the training data with each of the 10 test data values
'''

test_points = pida.test_df_to_coordinates_list(pikachu_test_data, pichu_test_data)

pikachu_classified = 0 #initialising values for how points are classified by following algorithm
pichu_classified = 0

for test_point in test_points : #each test point will be tested against it's 5 closest points in both datasets.
    pikachu_training_data = picalc.test_point_distance(test_point, pikachu_training_data)
    pichu_training_data = picalc.test_point_distance(test_point, pichu_training_data)
    pikachu_distances = pida.sort_and_list(pikachu_training_data) 
    pichu_distances = pida.sort_and_list(pichu_training_data)
    closer_matches = picalc.list_comparison(pikachu_distances,pichu_distances) # This as been the hardest of the exercice, comparing two lists, and extracting the minimal values to a correctly labelled dictionnary.

    if len(closer_matches['pikachu']) > len(closer_matches['pichu']):
        pikachu_classified += 1 #As the code is ran 10 times, I wanted to store all the outputs to get accuracy.
        print(f"Test point {test_point} classified as a pikachu ({len(closer_matches['pikachu'])} closer pikachus, {len(closer_matches['pichu'])} closer pichus)")
    else:
        pichu_classified += 1
        print(f"Test point {test_point} classified as a pichu ({len(closer_matches['pikachu'])} closer pikachus, {len(closer_matches['pichu'])} closer pichus)")

accuracy = (5 - (5 - pikachu_classified) + 5 -(5 - pichu_classified))/10
print(f"test points were classified as {pikachu_classified} pikachus and {pichu_classified} pichus. Expected 5 pikachus and 5 pichus, accuracy : {accuracy}")


'''
Void previous algorithm for classifying a test point based on a unique closest value.¢
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

