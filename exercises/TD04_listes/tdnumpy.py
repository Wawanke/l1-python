# Créé par christinefrodeau, le 10/11/2021 en Python 3.7
import numpy as np

carre_mag = [[4,  14, 15, 1],
             [9,  7,  6,  12],
             [5,  11, 10, 8],
             [16, 2,  3,  13]]

carre_non_mag = [[4,  14, 15, 1],
                 [9,  7,  6,  12],
                 [5,  11, 11, 8],
                 [16, 2,  7,  13]]

carre = [[1, 2],
         [2, 1]]

a = np.array(carre)

def test_carre_mag(carre):
    carre = np.array(carre)
    #Test lignes et colonnes
    num = np.ndarray.tolist(np.sum(carre, axis = 0))
    num += np.ndarray.tolist(np.sum(carre, axis = 1))

    #Test Diagonales
    #1ère diag
    a = np.ndarray.tolist(np.diagonal(carre))
    k = 0
    for i in a :
        k += i
    k = [k]
    num += k
    #2ème diag
    k1 = len(carre) - 1
    diag2 = 0
    for i in carre :
        diag2 += i[k1]
        k1 -= 1
    diag2 = [diag2]
    num += diag2

    #num est une liste comportant toutes les valeurs de sommes du carré
    verif = True
    for i in num :
        if num[0] == i :
            pass
        else :
            verif = False

    return verif

print(test_carre_mag(carre_mag))
print(test_carre_mag(carre_non_mag))




