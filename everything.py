# Affichage des formules
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
            EC_masse = float(input("Masse de l'objet :"))
            EC_vitesse = float(input("Vitesse de l'objet :"))
            Etot = (EC_masse / 2) * (EC_vitesse ** 2)
            print("L'énergie cinétique E = {:.2f} J".format(Etot))
        elif energie_cinetique == 2:
            EC_vitesse = float(input("Vitesse de l'objet :"))
            EC_energie = float(input("Energie cinétique de l'objet :"))
            masse = (2 * EC_energie) / (EC_vitesse ** 2)
            print("La masse de l'objet est de {:.2f} kg".format(masse))

        elif energie_cinetique == 3:
            EC_masse = float(input("Masse de l'objet :"))
            EC_energie = float(input("Energie cinétique de l'objet :"))
            vitesse = ((2 * EC_energie) / EC_masse) ** 0.5
            print("La vitesse de l'objet est de {:.2f} m/s".format(vitesse))

    elif energie == 2:
        print("Quelle variable cherchez-vous ?")
        print("1. E (en Joule)")
        print("2. M (en kg)")
        print("4. H (en m)")
        energie_potentielle = float(input("Indiquez votre choix :"))
        if energie_potentielle == 1:
            EP_masse = float(input("Masse de l'objet :"))
            EP_hauteur = float(input("Hauteur de l'objet :"))
            EP_gravite = float(input("Valeur de la gravité :"))
            Epot = EP_masse * EP_gravite * EP_hauteur
            print("L'énergie potentielle Ep = {:.2f} J".format(Epot))

        elif energie_potentielle == 2:
            EP_hauteur = float(input("Hauteur de l'objet :"))
            EP_gravite = float(input("Valeur de la gravité :"))
            EP_energie = float(input("Energie potentielle de l'objet :"))
            masse = EP_energie / (EP_gravite * EP_hauteur)
            print("La masse de lo'bjet est de {:.2f} kg".format(masse))
    elif energie == 3:
        print("Quelle variable cherchez-vous ?")
        print("1. E (en Joule)")
        print("2. Débit (en m³/s)")
        print("3. Hauteur (en m)")
        energie_hydrolique = float(input("Indiquez votre choix :"))
        if energie_hydrolique == 1:
            EH_debit = float(input("Débit de l'objet :"))
            EH_hauteur = float(input("Hauteur de l'objet :"))
            EH_poids_specifique = float(input("Poids spécifique du fluide :"))
            EH_energie = EH_debit * EH_hauteur * EH_poids_specifique
            print("L'énergie hydraulique E = {:.2f} J".format(EH_energie))
        elif energie_hydrolique == 2:
            EH_hauteur = float(input("Hauteur de l'objet :"))
            EH_poids_specifique = float(input("Poids spécifique du fluide :"))
            EH_energie = float(input("Energie hydraulique de l'objet :"))
            debit = EH_energie / (EH_hauteur * EH_poids_specifique)
            print("Le débit de l'objet est de {:.2f} m³/s".format(debit))
        elif energie_hydrolique == 3:
            EH_debit = float(input("Débit de l'objet :"))
            EH_poids_specifique = float(input("Poids spécifique du fluide :"))
            EH_energie = float(input("Energie hydraulique de l'objet :"))
            hauteur = EH_energie / (EH_debit * EH_poids_specifique)
            print("La hauteur de l'objet est de {:.2f} m".format(hauteur))

    elif energie == 4:
        print("Quelle variable cherchez-vous ?")
        print("1. E (en Joule)")
        print("2. Surface (en m²)")
        print("3. Rendement (en %)")
        print("4. Flux solaire incident")
        energie_photovoltaique = float(input("Indiquez votre choix :"))
        if energie_photovoltaique == 1:
            EPV_surface = float(input("Surface du panneau :"))
            EPV_rendement = float(input("Rendement du panneau :"))
            EPV_flux_solaire = float(input("Flux solaire incident :"))
            Epv = EPV_surface * EPV_rendement * EPV_flux_solaire
            print("L'énergie photovoltaïque E = {:.2f} J".format(Epv))

        elif energie_photovoltaique == 2:
            EPV_rendement = float(input("Rendement du panneau :"))
            EPV_flux_solaire = float(input("Flux solaire incident :"))
            EPV_energie = float(input("Energie photovoltaïque de l'objet :"))
            surface = EPV_energie / (EPV_rendement * EPV_flux_solaire)
            print("La surface du panneau est de {:.2f} m²".format(surface))

        elif energie_photovoltaique == 3:
            EPV_surface = float(input("Surface du panneau :"))
            EPV_flux_solaire = float(input("Flux solaire incident :"))
            EPV_energie = float(input("Energie photovoltaïque de l'objet :"))
            rendement = EPV_energie / (EPV_surface * EPV_flux_solaire) * 100
            print("Le rendement du panneau est de {:.2f} %".format(rendement))

        elif energie_photovoltaique == 4:
            EPV_surface = float(input("Surface du panneau :"))
            EPV_rendement = float(input("Rendement du panneau :"))
            EPV_energie = float(input("Energie photovoltaïque de l'objet :"))
            flux_solaire = EPV_energie / (EPV_surface * EPV_rendement)
            print(
                "Le flux solaire incident est de {:.2f} W/m²".format(flux_solaire))

        else:
            print("Choix non valide")
    else:
        print("Choix non valide")
if groupe == 2:
    print("1. Résistance thermique surfacique")
    print("2. Flux thermique")
    print("3. Echange thermique")
    print("4. Changement d'état")
    thermodynamique = float(input("Indiquez votre choix :"))
    if thermodynamique == 1:
        print("Quelle variable cherchez-vous ?")
        print("1. Rth (en K/W)")
        print("2. Epaisseur (en m)")
        print("3. Conductivité thermique (en W/mK)")
        resistance_thermique = float(input("Indiquez votre choix :"))
        if resistance_thermique == 1:
            epaisseur = float(input("Epaisseur (en mètre) :"))
            conductivité = float(input("Conductivité thermique (en W/mK):"))
            surface = float(input("Surface (en m²) :"))
            Rths = (epaisseur*surface)/conductivité
            print("Le résistance thermique Rths = {:.2f} K/W".format(Rths))
        elif resistance_thermique == 2:
            Rths = float(input("Résistance thermique (en K/W)) :"))
            conductivité = float(input("Conductivité thermique (en W/mK):"))
            surface = float(input("Surface (en m²) :"))
            epaisseur = (Rths*conductivité)/surface
            print("L'épaisseur E ' = {:.2f} m".format(epaisseur))
        elif resistance_thermique == 3:
            Rths = float(input("Résistance thermique (en K/W)) :"))
            epaisseur = float(input("Epaisseur (en mètre) :"))
            surface = float(input("Surface (en m²) :"))
            conductivité = (epaisseur*surface)/Rths
            print("La conductivité thermique ' = {:.2f} W/mK".format(conductivité))
    elif thermodynamique == 2:
        print("Quelle variable cherchez-vous ?")
        print("1. Q (en W)")
        print("2. S (en m²)")
        print("3. ΔT (en °C)")
        flux_thermique = float(input("Indiquez votre choix :"))
        if flux_thermique == 1:
            FT_S = float(input("Surface d'échange thermique (en m²) :"))
            FT_ΔT = float(input("Différence de température (en °C) :"))
            q = FT_S * FT_ΔT
            print("Le flux thermique q = {:.2f} W".format(q))
        elif flux_thermique == 2:
            FT_q = float(input("Flux thermique (en W) :"))
            FT_ΔT = float(input("Différence de température (en °C) :"))
            S = FT_q / FT_ΔT
            print("La surface d'échange thermique S = {:.2f} m²".format(S))
        elif flux_thermique == 3:
            FT_S = float(input("Surface d'échange thermique (en m²) :"))
            FT_q = float(input("Flux thermique(en W):"))
            FT_ΔT = float(input("Différence de température (en °C) :"))
            ΔT = FT_q / FT_S
            print("La différence de température ΔT = {:.2f} °C".format(ΔT))
        else:
            print("Choix invalide. Veuillez réessayer.")
    elif thermodynamique == 3:
        print("Quelle variable cherchez-vous ?")
        print("1. Cp (en J/kg.K)")
        print("2. m (en kg)")
        print("3. ΔT (en °C)")
        chaleur = float(input("Indiquez votre choix :"))
        if chaleur == 1:
            CH_m = float(input("Masse de l'échantillon (en kg) :"))
            CH_ΔT = float(input("Différence de température (en °C) :"))
            CH_q = float(input("Énergie échangée (en J) :"))
            Cp = CH_q / (CH_m * CH_ΔT)
            print("La capacité thermique massique Cp = {:.2f} J/kg.K".format(Cp))
        elif chaleur == 2:
            CH_Cp = float(input("Capacité thermique massique (en J/kg.K) :"))
            CH_ΔT = float(input("Différence de température (en °C) :"))
            CH_q = float(input("Énergie échangée (en J) :"))
            m = CH_q / (CH_Cp * CH_ΔT)
            print("La masse de l'échantillon m = {:.2f} kg".format(m))
        elif chaleur == 3:
            CH_Cp = float(input("Capacité thermique massique (en J/kg.K) :"))
            CH_m = float(input("Masse de l'échantillon (en kg) :"))
            CH_q = float(input("Énergie échangée (en J) :"))
            ΔT = CH_q / (CH_m * CH_Cp)
            print("La différence de température ΔT = {:.2f} °C".format(ΔT))
        else:
            print("Choix invalide. Veuillez réessayer.")