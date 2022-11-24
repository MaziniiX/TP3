import time
n=int(input("Veuillez saisir un nombre supérieur à 1 :"))
while n<1:
    n = int(input("Veuillez saisir un nombre supérieur à 1 :"))
print(n)
time.sleep(0.2)
#for i in range(n):
#    n=n-1
#    print(n)
#    time.sleep(0.2)
while n!=0:
    n=n-1
    print(n)
    time.sleep(0.2)