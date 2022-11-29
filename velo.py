heure_start = 0
heure_end = 0
ii = 0
l = 0
prix_double = 0
fin = False
boucle=0
while not fin:
    heure_start = int(input("Donnez l'heure de début de la location (un entier) : "))
    heure_end = int(input("Donnez l'heure de fin de la location (un entier) : "))
    if heure_start == heure_end:
        print(" Attention ! l’heure de fin est identique à l’heure de début.")
    elif heure_start > heure_end:
        print("Attention ! le début de la location est après la fin ...")
    elif 0 <= heure_start < 24 and 0 <= heure_end < 24:
        duree = heure_end - heure_start
        for i in range(duree+1):
            if heure_start >= 7 and heure_start < 17:
                heure_start = heure_start + 1
                ii = ii + 1
            else:
                l = l + 1
                heure_start = heure_start + 1
            boucle = True
        if boucle == True:
            prix_double += 2 * ii
            prix_total = prix_double + l
            print("Vous avez loué votre vélo pendant")
            if ii == 0:
                print("{} heure(s) au tarif horaire de 1.0 euro(s)".format(l))
                print("Le montant total à payer est de {} euro(s).".format(prix_total))
                fin = True
            elif l == 0:
                print("{} heure(s) au tarif horaire de 2.0 euro(s)".format(ii))
                print("Le montant total à payer est de {} euro(s).".format(prix_total))
                fin = True
            else:
                print("{} heure(s) au tarif horaire de 1.0 euro(s)".format(l))
                print("{} heure(s) au tarif horaire de 2.0 euro(s)".format(ii))
                print("Le montant total à payer est de {} euro(s).".format(prix_total))
                fin = True
    else:
        print("Les heures doivent être comprises entre 0 et 24 !")