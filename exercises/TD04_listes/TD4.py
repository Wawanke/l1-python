# Créé par christinefrodeau, le 20/10/2021 en Python 3.7

l = [3, 5, 10]
#print(l)

l += [12, 17]
#print(l)

l[2] = -7
#print(l)

for i in l:
    l[l.index(i)] = i * 2
#print(l)

for i in l :
    l[l.index(i)] = i + l.index(i)
#print(l)

import random
t = []
o = 0
for i in range(10):
    k = random.randint(10, 99)
    t.append(k)
    o += k
#print(t, " Total : ", o, " Maximum : ", max(t))
t1 = []
t2 = []
for i in t :
    if i % 2 == 0 :
        t1.append(i)
    else :
        t2.append(i)
#print("Tableau paire : ", t1, " et tableau impair : ", t2)

t3 = []
for i in t :
    t3.append(min(t))
    del t[t.index(min(t))]
#print(t3)

del t3[0]
del t3[-1]
#print(t3)

jeux_cartes = []
for i in range(52) :
    jeux_cartes.append(i + 1)
#print(jeux_cartes)

def coupe_jeux(jeux_cartes, ind): #Demande un indice
    return jeux_cartes[: ind], jeux_cartes[ind :]

#print(coupe_jeux(jeux_cartes, 4))


#2. Problème de Syracuse

def suite_syracuse(n):
    k = 0
    t = []
    while n != 1 :
        if n % 2 == 0 :
            n = n/ 2
        else :
            n = n * 3 + 1
        k += 1
        t.append(n)
    if t == [] :
        t = [0]
    return True, k, max(t)
#print(suite_syracuse(3))

def test_conjecture(n) :
    return suite_syracuse(n)

#print(test_conjecture(10000))

def temps_de_vol(returnn):
    return returnn[1]

#print(temps_de_vol(suite_syracuse(10000)))

def temps_vol_liste(n_max):
    t = []
    t1 = []
    for i in range (n_max):
        t.append(i + 1)
    for i in t :
        x1 = suite_syracuse(i)
        x = temps_de_vol(x1)
        t1.append(x)
    return t1
x1 = 10000
#print(temps_vol_liste(x1))
#print(max(temps_vol_liste(x1)))

def altitude_vol(n_max):
    t = []
    t1 = []
    t2 = []
    for i in range (n_max):
        t.append(i + 1)
    for i in t :
        x1 = suite_syracuse(i)
        x = temps_de_vol(x1)
        t1.append(x)
        x1 = suite_syracuse(i)
        t2.append(x1[2])
    return "Altitude de vol : ", max(t2)

#print(altitude_vol(x1))

#Carré magique
"""
carre_mag = [[4,  14, 15, 1],
             [9,  7,  6,  12],
             [5,  11, 10, 8],
             [16, 2,  3,  13]]

carre_non_mag = [[4,  14, 15, 1],
             [9,  7,  6,  12],
             [5,  11, 10, 8],
             [16, 2,  7,  13]]

c = carre_mag
c1 = c[0][0] + c[0][1] + c[0][2] + c[0][3]
c2 = c[0][0] + c[1][1] + c[2][2] + c[3][3]
c3 = c[0][0] + c[1][0] + c[2][0] + c[3][0]

if c1 == c2 and c2 == c3 and c1 == c3 :
    print("La constante magique est : ", c1)
"""

carre_mag = [[4,  14, 15, 1],
             [9,  7,  6,  12],
             [5,  11, 10, 8],
             [16, 2,  3,  13]]

carre_non_mag = [[4,  14, 15, 1],
                 [9,  7,  6,  12],
                 [5,  11, 11, 8],
                 [16, 2,  7,  13]]

def affiche_carre(carre):
    k = 0
    for i in carre :
        str_ = "[" + str(carre[k][0]) + " " + str(carre[k][1]) + " " + str(carre[k][2]) + " " + str(carre[k][3]) + "]"
        print(str_)
        k += 1

#affiche_carre(carre_mag)
#print("")
#affiche_carre(carre_non_mag)

def test_sommes_carre(carre):
    k = 0
    k1 = 3
    diag1, diag2, x2, x3, x4, x5 = 0, 0, 0, 0, 0, 0
    t = []
    for i in carre :
        #Test lignes
        x = i[0] + i[1] + i[2] + i[3]
        t.append(x)
        #Test diagonales
        diag1 += i[k]
        diag2 += i[k1]
        k += 1
        k1 -= 1
        #Test colonnes
        x2 += i[0]
        x3 += i[1]
        x4 += i[2]
        x5 += i[3]
    t1 = [diag1, diag2]
    t2 = [x2, x3, x4, x5]
    return t, t1, t2

def est_carre_mag(carre) :
    test = True
    c1 = test_sommes_carre(carre)
    c1 = c1[0] + c1[1] + c1[2]
    for i in c1 :
        if i == c1[0] :
            test = True
        else :
            return False
    return test

assert est_carre_mag(carre_mag) == True, "Petit problème là"
assert est_carre_mag(carre_non_mag) == False, "Petit problème là"

def estNormal(carre):
    t_nb = []
    for i in carre :
        for u in i :
            t_nb.append(u)
    for i in range(len(t_nb)) :
        i += 1
        if i == min(t_nb) :
            del t_nb[t_nb.index(i)]
        else :
            return "Carré pas normal"
    if t_nb == [] :
        return "Carré normal"

#print(estNormal(carre_mag))
#print(estNormal(carre_non_mag))











