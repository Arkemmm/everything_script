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
    elif energie == 3:
        print("Quelle variable cherchez-vous ?")
        print("1. E (en Joule)")
        print("2. Débit (en m³/s)")
        print("3. Hauteur (en m)")
        energie_hydrolique = float(input("Indiquez votre choix :"))
        if energie_hydrolique == 1:
            EH_debit= float(input("Débit de l'objet :"))
            EH_hauteur= float(input("Hauteur de l'objet :"))
            EH_poids_specifique= float(input("Poids spécifique du fluide :"))
            EH_energie = EH_debit * EH_hauteur * EH_poids_specifique
            print("L'énergie hydraulique E = {:.2f} J".format(EH_energie))
        elif energie_hydrolique == 2:
            EH_hauteur= float(input("Hauteur de l'objet :"))
            EH_poids_specifique= float(input("Poids spécifique du fluide :"))
            EH_energie= float(input("Energie hydraulique de l'objet :"))
            debit = EH_energie / (EH_hauteur * EH_poids_specifique)
            print("Le débit de l'objet est de {:.2f} m³/s".format(debit))
        elif energie_hydrolique == 3:
            EH_debit= float(input("Débit de l'objet :"))
            EH_poids_specifique= float(input("Poids spécifique du fluide :"))
            EH_energie= float(input("Energie hydraulique de l'objet :"))
            hauteur = EH_energie / (EH_debit * EH_poids_specifique)
            print("La hauteur de l'objet est de {:.2f} m".format(hauteur))

    elif energie == 4:
        print("Quelle variable cherchez-vous ?")
        print("1. E (en Joule)")
        print("2. Surface (en m²)")
        print("3. Rendement (en %)")
        energie_photovoltaique = float(input("Indiquez votre choix :"))
        if energie_photovoltaique == 1:
            EPV_surface= float(input("Surface du panneau :"))
            EPV_rendement= float(input("Rendement du panneau :"))
            EPV_flux_solaire= float(input("Flux solaire incident :"))
            Epv = EPV_surface * EPV_rendement * EPV_flux_solaire
            print("L'énergie photovoltaïque E = {:.2f} J".format(Epv))

        elif energie_photovoltaique == 2:
            EPV_rendement= float(input("Rendement du panneau :"))
            EPV_flux_solaire= float(input("Flux solaire incident :"))
            EPV_energie= float(input("Energie photovoltaïque de l'objet :"))
            surface = EPV_energie / (EPV_rendement * EPV_flux_solaire)
            print("La surface du panneau est de {:.2f} m²".format(surface))

        elif energie_photovoltaique == 3:
            EPV_surface= float(input("Surface du panneau :"))
            EPV_flux_solaire= float(input("Flux solaire incident :"))
            EPV_energie= float(input("Energie photovoltaïque de l'objet



