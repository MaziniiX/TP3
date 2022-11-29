cycle=0
calcul=1
n=int(input("Veuillez saisir un entier n: "))
type=str(input("Ecrivez W pour utiliser une boucle while, ou écrivez F pour utiliser une boucle for: "))
if type=="W" or type=="w":
    print("Vous avez choisi d'utiliser while")
    while cycle!=n:
        cycle=cycle+1
        calcul=calcul*cycle
        print("itération n°{} || factorielle égal à: {}".format(cycle,calcul))
elif type=="F" or type=="f":
    print("Vous avez choisi d'utiliser for")
    for i in range(n):
        cycle=cycle+1
        calcul=calcul*cycle
        print("itération n°{} || factorielle égal à: {}".format(cycle,calcul))