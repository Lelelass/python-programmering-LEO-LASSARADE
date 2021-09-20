
def test_point_distance(test_point, data):
    data['distance']  = ((data['Width'] - test_point[0])**2 + (data['Height'] - test_point[1])**2)**0.5
    return data

def list_comparison(pika_closest_points, pichu_closest_points):# Returns the 5 smallest values of two distinct lists. Just fitted for the program's application. Not general.
    closer_matches = {"pikachu" : [], "pichu": []} 
    i = 0

    while i < 5 and len(closer_matches['pikachu']) + len(closer_matches['pichu']) < 5:
        j = 0
        append_pika = True

        while j < len(pichu_closest_points):
            if pika_closest_points[i] < pichu_closest_points[j]:
                j += 1
            else:
                closer_matches['pichu'].append(pichu_closest_points[j])
                #if i != 0:
                #    i -= 1
                if j + 1 < len(pichu_closest_points) and pika_closest_points[i] < pichu_closest_points[j+1]:
                    closer_matches['pikachu'].append(pika_closest_points[i])
                append_pika = False
                pichu_closest_points.remove(pichu_closest_points[j])
                break
        
        if append_pika != False:
            closer_matches['pikachu'].append(pika_closest_points[i])
        
        i += 1

    return closer_matches
