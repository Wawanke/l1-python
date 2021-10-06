# Créé par christinefrodeau, le 29/09/2021 en Python 3.7

#Exo 1
"""
def facteur(b, c) :
    if b % c == 0 :
        return "FACTEURRRRRRR"
    elif b % 2 != 0 :
        return "pas facteur"

b = 15
c = 2

assert facteur(b, c) == "pas facteur", "oupsi"
"""

#Exo 2
"""
tab_ville = ["new jersey", "north carolina", "georgia"]
tab_etat = ["School isn't cancelled.", "School is postponed.", "School is cancelled!"]

def ville_etat (v):
    for i in tab_ville :
        if i == v :
            u = tab_ville.index(i)
            return tab_etat[u]
        else :
            return "School's status is unknown"

assert ville_etat(tab_ville[0]) == tab_etat[0], "oupsi"
assert ville_etat(tab_ville[1]) == tab_etat[1], "oupsi"
assert ville_etat(tab_ville[2]) == tab_etat[2], "oupsi"
"""

#Exo 3
"""
d = {0: "monkey",
     1: "rooster",
     2: "dog",
     3: "pig",
     4: "rat",
     5: "ox",
     6: "tiger",
     7: "rabbit",
     8: "dragon",
     9: "snake",
     10: "horse",
     11: "sheep"}

def zodiaque_chinois(o):
    u = o % 12
    for i in d :
        if i == u :
            return "Year of the " + d[u]

print(zodiaque_chinois(2003))
"""

#Exo 4
"""
def temperature_(temperature, celsius):
    if celsius == True :
        if temperature <= 0 :
            print("Freezing")
        else :
            print("not Freezing")
    else :
        if temperature <= 32 :
            print("Freezing")
        else :
            print("not Freezing")


temperature = 26
celsius = True
temperature_(temperature,celsius)
"""

#Exo 5
"""
def annee_bissextile(A):
    if A % 4 == 0 :
        print("A est une année bissextile")
    else :
        print("A n'est pas une année bissextile")

annee_bissextile(2000)
"""

#Exo 6
"""
t = list(range(20))
def pair(t):
    t_pair = []
    for i in t :
        if i % 2 == 0 :
            t_pair.append(i)
    return t_pair
print(pair(t))
"""

#Exo 7
"""
def saisie_nb():
    t = []
    k = 0
    n = int(input("Cmb de nb ?"))
    while n != 0 :
        o = int(input())
        t.append(o)
        k += o
        n -= 1
    return k / len(t)

print(saisie_nb())
"""

#Avec infinie jusqu'à avoir marqué -1
"""
def saisie_nb1():
    t = []
    k = 0
    while True :
        o = int(input())
        t.append(o)
        if o == -1 :
            break
        k += o

    return k / len(t)

print(saisie_nb1())
"""

#Exo 8

#Factoriel ?

#Exo 9
"""
Set1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
Set2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
Set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
Set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
Set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

def born_day():
    k = 0
    if input("Présent dans set 1 ? Réponse : y ou n ") == "y" :
        k += Set1[0]
    if input("Présent dans set 2 ? Réponse : y ou n ") == "y" :
        k += Set2[0]
    if input("Présent dans set 3 ? Réponse : y ou n ") == "y" :
        k += Set3[0]
    if input("Présent dans set 4 ? Réponse : y ou n ") == "y" :
        k += Set4[0]
    if input("Présent dans set 5 ? Réponse : y ou n ") == "y" :
        k += Set5[0]
    return "Le " + str(k) + " est ton jour de naissance"

print(born_day())
"""

#Exo 10
"""
import random
def loterie ():
    o = 0
    u = 10
    nb_client = int(input("Votre numéro (entre 0 et 100) "))
    nb_gagnant = random.randint(0, 100)
    nb_client_str = str(nb_client)

    N1 = str(nb_gagnant)[0]
    N2 = str(nb_gagnant)[1]
    n1 = nb_client_str[0]
    n2 = nb_client_str[1]
    print(N1, N2, n1, n2)

    if nb_client == nb_gagnant :
        return "Vous avez gagné le lot de 10000 euros (quechi)"
    if N1 == n2 and N2 == n1 :
        return "Vous avez gagné le lot 3000 euros"
    if N1 == n1 or N1 == n2 or N2 == n1 or N2 == n2 :
        return "Vous avez gagné le lot 1000 euros"

r = loterie()
if r == None :
    print("Perdu")
else :
    print(r)
"""

#Exo 11
"""
def calcul_inter_nb():
    nb = int(input("Votre nombre, entre 10 et 20 : "))
    n1 = int(str(nb)[0])
    n2 = int(str(nb)[1])
    return n1 + n2
print(calcul_inter_nb())
"""

#Exo 12
"""
import random

def test_maths():
    nb1 = random.randint(0, 9)
    nb2 = random.randint(0, 9)
    if nb1 <= nb2 :
        rep = nb2 - nb1
        str1 = "Combien font : " + str(nb2) + " - " + str(nb1) + " ? "
    else :
        rep = nb1 - nb2
        str1 = "Combien font : " + str(nb1) + " - " + str(nb2) + " ? "
    rep_utilisateur = False
    print(rep)
    while rep_utilisateur != True :
        rep_nb_u = int(input(str1))

        if rep_nb_u == rep :
            rep_utilisateur = True

print(test_maths())
"""

#Exo 13
"""
# A faire : Ecrire un programme qui permet de calculer le nombre de mots dans une phrase saisie par l'utilisateur.
# Comment faire : compter les espaces entre chaque mot, puis mot = espaces + 1

def nb_mot():
    str_ = str(input("Insérer phrase "))
    k = 0
    for i in str_ :
        if i == " " :
            k += 1
    return k + 1

print(nb_mot())
"""

#Exo 15
"""
def team_score():
    t_1 = "Team alpha"
    t_2 = "Team Beta"
    t_1_score = int(input("Score de " + t_1))
    t_2_score = int(input("Score de " + t_2))
    if t_1_score < t_2_score :
        gagnant = True
        winner = t_2
        loser = t_1
        winner_s = t_2_score
        loser_s = t_1_score
    elif t_1_score > t_2_score :
        gagnant = True
        winner = t_1
        loser = t_2
        winner_s = t_1_score
        loser_s = t_2_score
    else :
        winner_s = 0
        loser_s = 0
        gagnant = False
    margin = winner_s - loser_s
    if gagnant == True :
        return winner + " a batu " + loser + " de : " + str(margin)
    else :
        return t_1 + " a joué " + t_2 + ", cela s'est finie en match nul, avec : " + str(t_1_score) + " à " + str(t_2_score)
print(team_score())
"""

#Exo 16
"""
def imc () :
    uni_poids = input("Quelle est votre poids (kg ou pounds) : ")
    if uni_poids == "kg" :
        masse = input("Votre poids (en kg) : ")
    else :
        masse = 0.45359237 * float(input("Votre poids (en pounds) : "))
    if uni_poids == "kg" :
        taille = input("Votre taille (en m) : ")
    else :
        taille = 0.0254 * float(input("Votre taille (en inch) : "))
    print (masse, taille )
    IMC = float(format(int(masse)/float(taille)**2, ".2f"))
    if IMC < 18.5 :
        return "Vous êtes en sous-poids"
    elif 18.5 < IMC < 24.9 :
        return "Vous êtes à un poids classique"
    elif 25 < IMC < 29.9:
        return "Vous êtes en surpoids"
    else:
        return "Vous êtes en obésité"

print(imc())
"""

#Exo 17
"""
def affi_tri (nb):
    k = 0
    str_ = ""
    while k != nb :
        str_ += "*"
        print(str_)
        k += 1
nb = 6
affi_tri(nb)
"""

#Exo 18
"""
def affi_tri_inverse(nb) :
    k = nb
    str_ = ""
    while k != 0 :
        str_ = ""
        for i in range(k-1) :
            str_ += " "
        for i in range(nb - (k-1)) :
            str_ += "*"
        print(str_)
        k -= 1
nb = 6
affi_tri_inverse(nb)
"""

#Exo 19
"""
def multiple_million ():
    nb = int(input("Votre nombre : "))
    k = 0
    pui = 0
    tab = []
    while k < 1000000 :
        k = nb **pui
        tab.append(k)
        pui += 1
    return "Voici la plus grand nombre en dessous d'un million pour : " + str(nb) + ", " + str(tab[-2]) + " soit puissance : " + str(pui - 2)
print(multiple_million())
"""























































