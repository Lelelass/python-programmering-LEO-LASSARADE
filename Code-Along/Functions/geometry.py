def triangle_area(base, height):
    area = (base * height)/2
    return area

def eucl_dist(P,Q):
    distance = math.sqrt((P[0]-Q[0])**2 + (P[1]-Q[1])**2)
    return distance