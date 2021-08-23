import math

'''1'''
a, b = 3, 4
c = math.sqrt(a ** 2 + b ** 2)

print(c)

'''2'''
c2, a2 = 7, 5
b2 = round(math.sqrt(c2 ** 2 - a2 ** 2), 2)

print(b2)

'''3'''

def accuracy (TP, TN, FP, FN):
    return (sumTPTN := TP + TN) / (sumTPTN + FP + FN)

print(accuracy(2,985,2,11))