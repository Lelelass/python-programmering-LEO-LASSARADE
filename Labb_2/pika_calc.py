import pandas as pd

def test_point_distance(test_point: list, data: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a column to the dataframe with the values of euclidian distances calculus from a given test point
    """
    data['distance']  = ((data['Width'] - test_point[0])**2 + (data['Height'] - test_point[1])**2)**0.5
    return data

def list_comparison(pika_closest_points: list, pichu_closest_points: list) -> dict:
    '''
    Returns the 5 smallest values of two distinct lists into a dict.
    Just fitted for the program's application. Not general.
    '''  
    closer_matches = {"pikachu" : [], "pichu": []} 
    i = 0

    while i < 5 and len(closer_matches['pikachu']) + len(closer_matches['pichu']) < 5: #Insure to loop through all i values, and that only 5 values end up in the dictionnary
        j = 0
        append_pika = True

        while j < len(pichu_closest_points): #condition as a variable here, as items are sometimes removed from the second list. Avoids out of range error.
            if pika_closest_points[i] < pichu_closest_points[j]:
                j += 1
            else:
                closer_matches['pichu'].append(pichu_closest_points[j])

                if j + 1 < len(pichu_closest_points) and pika_closest_points[i] < pichu_closest_points[j+1]:
                    closer_matches['pikachu'].append(pika_closest_points[i])
                elif i != 0:
                    i -= 1 # I chosed a while loop approach with i and j indexes to be able to get back, not possible in a for loop.
                append_pika = False
                pichu_closest_points.remove(pichu_closest_points[j])
                break
        
        if append_pika != False:
            closer_matches['pikachu'].append(pika_closest_points[i])
        
        i += 1

    return closer_matches
