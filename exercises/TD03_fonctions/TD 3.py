# Créé par christinefrodeau, le 06/10/2021 en Python 3.7

#Exo 1

def temps_en_sec(t):
    return t[3] + t[2] * 60 + t[1] * 3600 + t[0] * 8640

t = (4, 3, 13, 20)
print(temps_en_sec(t))

t1 = temps_en_sec(t)

def sec_en_temps(sec):
    """
    d = sec % 60
    c1 = sec // 60
    c = c1 % 60
    print(c1, c)
    b1 = c1 // 60
    b = b1 % 60
    print(b1, b)
    a = 0
    tab = [a, b, c, d]
    tab_affi = ()
    tab_affi = (tab[0], tab[1], tab[2], tab[3])
    return tab_affi"""

    #TESTTTTTTT
    reste = sec % 60
    minutes = reste / 60

    reste = reste % 3600
    heures = reste / 3600

    reste = reste % (3601 * 24)
    jours = reste / (3600 * 24)

    p = (jours, heures, minutes, sec)
    return p

secs = 36440
print(sec_en_temps(secs))













