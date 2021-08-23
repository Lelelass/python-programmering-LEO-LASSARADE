import math

'''1'''
a, b = 3, 4
c = math.sqrt(a ** 2 + b ** 2)

print(c)

c2, a2 = 7, 5
c2square = c2 ** 2
a2square = a2 ** 2

b2 = round(math.sqrt(c2square - a2square), 2)

print(b2)

'''3'''

def accuracy (TP, TN, FP, FN):
    return (sumTPTN := TP + TN) / (sumTPTN + FP + FN)

print(accuracy(2,985,2,11))