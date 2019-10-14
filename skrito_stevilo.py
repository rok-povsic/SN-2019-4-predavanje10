import random

skrito_stevilo = random.randint(1, 100)

with open("tocke.txt") as datoteka:
    stari_stevec = int(datoteka.read())

print("Prejšnje število poskusov je bilo: " + str(stari_stevec))

stevec = 0
while True:
    vneseno_stevilo = int(input("Ugani število: "))
    stevec += 1

    if vneseno_stevilo == skrito_stevilo:
        print("Čestitke, uganili ste pravo število")
        break
    elif vneseno_stevilo > skrito_stevilo:
        print("Vpisali ste preveliko število")
    else:
        print("Vpisali ste premajhno število")

print("Število poskusov je bilo: " + str(stevec))

if stevec < stari_stevec:
    with open("tocke.txt", "w") as datoteka:
        datoteka.write(str(stevec))

print("Konec programa")