import numpy as np



def KNN(X_N, Y_N, X_P, Y_P, X_O, Y_O, K, X_T, Y_T):

    X_Negatief = X_N
    Y_Negatief = Y_N
    X_Positief = X_P
    Y_Positief = Y_P
    X_Onbekend = X_O
    Y_Onbekend = Y_O

    K = K
    X_Test = X_T
    Y_Test = Y_T

    Distance_Negatief = []
    Distance_Positief = []
    Distance_Onbekend = []

    for n in range(len(X_Negatief)):
        D = ((X_Test - X_Negatief[n])**2 + (Y_Test - Y_Negatief[n])**2)**0.5
        Distance_Negatief.append(D)

    for p in range(len(X_Positief)):
        D = ((X_Test - X_Positief[p])**2 + (Y_Test - Y_Positief[p])**2)**0.5
        Distance_Positief.append(D)

    for o in range(len(X_Onbekend)):
        D = ((X_Test - X_Onbekend[o])**2 + (Y_Test - Y_Onbekend[o])**2)**0.5
        Distance_Onbekend.append(D)

    R = []

    for k in range(K):
        compare = [min(Distance_Negatief),min(Distance_Positief),min(Distance_Onbekend)]
        if compare[0] == min(compare):
            R.append('Negatief')
            Distance_Negatief.remove(min(Distance_Negatief))
        if compare[1] == min(compare):
            R.append('Positief')
            Distance_Positief.remove((min(Distance_Positief)))
        if compare[2] == min(compare):
            R.append('Onbekend')
            Distance_Onbekend.remove(min(Distance_Onbekend))
    status = max(R, key=R.count)
    return status





























