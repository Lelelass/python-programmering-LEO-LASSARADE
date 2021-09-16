import math
from statistics import mean

def eucl_dist(P,Q):
    distance = math.sqrt((P[0]-Q[0])**2 + (P[1]-Q[1])**2)
    return distance


def test_point_distance(test_point, data):
    distances = []
    for index, row in data.iterrows():
        distances.append(eucl_dist(test_point,(row['Width'],row['Height'])))
    return mean(distances) # https://www.geeksforgeeks.org/find-average-list-python/
