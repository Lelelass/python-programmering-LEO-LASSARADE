
def test_point_distance(test_point, data):
    data['distance']  = ((data['Width'] - test_point[0])**2 + (data['Height'] - test_point[1])**2)**0.5
    return data
    #return data['distance'].min()# Minimal value for column distance

