import random

vies = 15
nb = random.randrange(1, 10000)
choix = int(input("Choisi un nombre entre 0 et 10000: "))
partie = True

while partie:
    while vies != 0:

        if choix < nb:
            print("Plus grand")
            vies -= 1
            if vies > 1:
                print("Nombre de vies restantes = {} ".format(vies))
            else:
                print("Nombre de vie restante = {} ".format(vies))

            choix = int(input("Recommence: "))
            continue

        if choix > nb:
            print("Plus petit")
            vies -= 1
            if vies > 1:
                print("Nombre de vies restantes = {} ".format(vies))
            else:
                print("Nombre de vie restante = {} ".format(vies))
            choix = int(input("Recommence: "))
            continue

        else:
            print("Vous avez gagné")
            partie = False
            break

    else:
        print("Vous avez perdu")
        partie = False

