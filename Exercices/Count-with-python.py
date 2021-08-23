import math

'''1'''
a, b = 3, 4
c = math.sqrt(a ** 2 + b ** 2)

print("1a : " + c)

'''1b'''
c2, a2 = 7, 5
b2 = round(math.sqrt(c2 ** 2 - a2 ** 2), 2)

print("1b : " + b2)


''''2'''

'''3'''

def accuracy (TP, TN, FP, FN):
    return (sumTPTN := TP + TN) / (sumTPTN + FP + FN)

print("Accuracy:" + accuracy(2,985,2,11))