#Affichage des formules
print("Groupe de relations")
print("1. Calculs d'énergie")
print("2. Thermodynamique")
print("3. Mécanique")
print("4. Courrants et signaux")
print("5. Géométrie")

groupe = float(input("Indiquez votre choix :"))

if groupe == 1:
    print("1. Energie cinétique")
    print("2. Energie potentiel de pesanteur")
    print("3. Energie hydrolique")
    print("4. Energie photovoltaïque")

    energie = float(input("Indiquez votre choix :"))
    if energie == 1:
        print("Quelle variable cherchez-vous ?")
        print("1. E (en Joule)")
        print("2. M (en kg)")
        print("3. V (en m/s)")
        energie_cinetique = float(input("Indiquez votre choix :"))
        if energie_cinetique == 1:
            EC_masse= float(input("Masse de l'objet :"))
            EC_vitesse= float(input("Vitesse de l'objet :"))
            Etot = (EC_masse / 2) * (EC_vitesse ** 2)
            print("L'énergie cinétique E = {:.2f} J".format(Etot))
            

