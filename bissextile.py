# -*-coding:Utf-8 -*

print("\nDéterminons si une année est bissextile sur la période allant de 0 à 9999 après JC.")
print("Une année bissextile comprend 366 jours au lieu des 365 habituels.")
print("Appuyer sur la touche 'q' pour quitter.\n")

continuer = True

while continuer:
    année = input("Choisissez une année : ")
    if année == 'q':
        print("Merci d'avoir utilisé ce programme.")
        continuer = False
    else:
        try:
            an = int(année)
            if (an >= 0 and an <= 9999):
                if (an % 4 == 0 and an % 100 != 0):
                    print("Oui, " + str(an) + " est bien une année bissextile.")
                elif (an % 400 == 0):
                    print("Oui, " + str(an) + " n'est pas une année bissextile.")
                else:
                    print("Non, " + str(an) + " n'est pas une année bissextile.")
        except:
            print("Veuillez entrer une valeur correcte.")
