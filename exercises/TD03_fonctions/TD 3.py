# Créé par christinefrodeau, le 06/10/2021 en Python 3.7

#Exo 1

def temps_en_sec(t):
    return t[3] + t[2] * 60 + t[1] * 3600 + t[0] * 86400

t = (4, 3, 13, 20)
#print(temps_en_sec(t))

t1 = temps_en_sec(t)

def sec_en_temps(sec):

    d1 = sec % 60
    d2 = sec // 60
    d3 = d2 // 60
    d4 = d3 //24
    c = d2 % 60
    b = d3 % 24
    a = d3 // 24
    tab = tuple([a, b, c, d1])
    tab_affi = (tab[0], tab[1], tab[2], tab[3])
    return tab_affi
print
secs = 46160
#print(sec_en_temps(t1))
#temps = sec_en_temps(t1)

def affi_tps (temps):
    t = [temps[0], temps[1], temps[2], temps[3]]
    t_singu = [" jour ", " heure ", " minute ", ' seconde ']
    t_plu = [" jours ", " heures ", " minutes ", " secondes "]
    for i in t :
        index_i = t.index(i)
        if i == 0 :
            pass
        elif i == 1 :
            print(str(i) + t_singu[index_i], end = "")
            t[index_i] = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        else :
            print(str(i) + t_plu[index_i], end= "")

#affi_tps((1, 0, 3, 1))


def demande_temps():
    a = int(input("Insérer le nombre de jour(s) : "))
    b = int(input("Insérer le nombre d'heure(s) : "))
    c = int(input("Insérer le nombre de minute(s) : "))
    d = int(input("Insérer le nombre de seconde(s) : "))
    return (a, b, c, d)

#affi_tps(j)

def somme_temps(tps1, tps2):
    t_somme = temps_en_sec(tps1) + temps_en_sec(tps2)
    return sec_en_temps(t_somme)

#print(somme_temps((4, 3, 13, 20), (4, 3, 13, 20)))

def proportionTemps(temps, proportion):
    return sec_en_temps(temps_en_sec(temps) * proportion)

#affi_tps(proportionTemps((2,0,36,0),0.2))


def tempsEnDate(temps):
    if type(temps) == type(tuple()) :
        sec = temps_en_sec(temps)
    elif type(temps) == type(int()) :
        sec = temps
    d = sec % 60
    c1 = sec // 60
    c = c1 % 60
    b1 = c1 // 60
    b = b1 % 24
    a1 = b1 //24
    a = a1 % 365
    e1 = a1 // 365
    e = a1 //365
    tab = [e, a, b, c, d]
    print()
    return tab

def afficheDate(temps):
    t = [temps[0], temps[1], temps[2], temps[3], temps[4]]
    t_singu = [" ans ", " jour ", " heure ", " minute ", ' seconde ']
    t_plu = [" années ", " jours ", " heures ", " minutes ", " secondes "]
    for i in t :
        index_i = t.index(i)
        if i == 0 :
            pass
        elif i == 1 :
            print(str(i) + t_singu[index_i], end = "")
            t[index_i] = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        else :
            print(str(i) + t_plu[index_i], end= "")
            t[index_i] = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000



temps1 = sec_en_temps(31622478)
#print(temps1)
#print(affi_tps(temps1), "\n")
#afficheDate(tempsEnDate(temps1))
#print(tempsEnDate(temps1))

import time
#print(time.gmtime(31622478))
#print("50 ans = 1576800000")

def bisextile(jour):
    s = temps_en_sec((jour, 0, 0, 0))
    s1 = s + 1576800000
    tab = time.gmtime(s1)
    t = tab[0] #ressort juste un int :D et pas du str
    o = (t - 2020) // 4
    t = []
    k = 2020
    i = 0
    while i != o :
        k += 4
        t.append(k)
        i += 1
    return t

#print(bisextile(20000)) #C'est donné en jours !!!


def seconde_verif_bisextile(sec): #Prend des secondes
    return int(sec / 86400) % 4

def tempsEnDateBisextile(temps):
    tupl = (temps[1], temps[2], temps[3], temps[4])
    p = temps[0] * 31536000 + temps_en_sec(tupl)
    print(type(p))
    o = time.gmtime(p)
    l = o[2]
    temps = (temps[0], o, temps[1], temps[2], temps[3], temps[4])
    if seconde_verif_bisextile(temps_en_sec((temps[0], 0, 0, 0))) == 0 :
        return "cestBON"
    else :
        return temps

temps = tempsEnDate((365*2000, 1, 2, 3))
#afficheDate(temps)
#afficheDate(tempsEnDateBisextile(temps))
print(tempsEnDateBisextile(temps))







