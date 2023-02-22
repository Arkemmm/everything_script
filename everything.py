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
        elif energie_cinetique == 2:
            EC_vitesse= float(input("Vitesse de l'objet :"))
            EC_energie= float(input("Energie cinétique de l'objet :"))
            masse = (2 * EC_energie) / (EC_vitesse ** 2)
            print("La masse de l'objet est de {:.2f} kg".format(masse))

        elif energie_cinetique == 3:
            EC_masse= float(input("Masse de l'objet :"))
            EC_energie= float(input("Energie cinétique de l'objet :"))
            vitesse = ((2 * EC_energie) / EC_masse) ** 0.5
            print("La vitesse de l'objet est de {:.2f} m/s".format(vitesse))

    elif energie == 2:
        print("Quelle variable cherchez-vous ?")
        print("1. E (en Joule)")
        print("2. M (en kg)")
        print("4. H (en m)")
        energie_potentielle = float(input("Indiquez votre choix :"))
        if energie_potentielle == 1:
            EP_masse= float(input("Masse de l'objet :"))
            EP_hauteur= float(input("Hauteur de l'objet :"))
            EP_gravite= float(input("Valeur de la gravité :"))
            Epot = EP_masse * EP_gravite * EP_hauteur
            print("L'énergie potentielle Ep = {:.2f} J".format(Epot))

        elif energie_potentielle == 2:
            EP_hauteur= float(input("Hauteur de l'objet :"))
            EP_gravite= float(input("Valeur de la gravité :"))
            EP_energie= float(input("Energie potentielle de l'objet :"))
            masse = EP_energie / (EP_gravite * EP_hauteur)
            print("La masse de lo'bjet est de {:.2f} kg".format(masse))


