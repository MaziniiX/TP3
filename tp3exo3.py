import random
essai=1
nombre=random.randint(0, 100)
guess=0
print(nombre)
while guess!=nombre:
    guess=int(input("Essayez de deviner le nombre entre 0 et 100:"))
    if guess<nombre:
        print("Plus grand!")
        essai = essai + 1
    elif guess>nombre:
        print("Plus petit!")
        essai=essai+1
print("Vous avez devinez le nombre en",essai,"essais")