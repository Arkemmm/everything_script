import math
# Les constantes
pi = 3.14159265359
g = 9,80665
c = 299792458
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
    print("3. Puissance hydraulique")
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
        print("1. P (en W)")
        print("2. Débit (en m³/s)")
        print("3. Δh (en m)")
        puissance_hydraulique = float(input("Indiquez votre choix :"))
        if puissance_hydraulique == 1:
            d = float(input("Débit (en m³/s) :"))
            h = float(input("Δh  (en m) :"))
            mv = float(input("Masse volumique du fluide :"))
            P = d*g*h*mv
            print("La puissance hydraulique P = {:.3e} W".format(P))
        elif puissance_hydraulique == 2:
            P = float(input("Puissance hydraulique (en W) :"))
            h = float(input("Δh  (en m) :"))
            mv = float(input("Masse volumique du fluide :"))
            d = P/(h*g*mv)
            print("Le débit de l'objet est de {:.2f} m³/s".format(d))
        elif puissance_hydraulique == 3:
            P = float(input("Puissance hydraulique (en W) :"))
            d = float(input("Débit (en m³/s) :"))
            mv = float(input("Masse volumique du fluide :"))
            h = P/(d*g*mv)
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
            print("Le flux solaire incident est de {:.2f} W/m²".format(flux_solaire))
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
        print("\n Quelle variable cherchez-vous ?")
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
        print("\n Quelle variable cherchez-vous ?")
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
        print("\n Quelle variable cherchez-vous ?")
        print("1. E (en J)")
        print("1. C (en J/kg.K)")
        print("2. m (en kg)")
        print("3. ΔT (en °C)")
        chaleur = float(input("Indiquez votre choix :"))
        if chaleur == 1:
            m = float(input("Masse (en kg) :"))
            t = float(input("Différence de température (en °C) :"))
            c = float(input("Capacité thermique massique (en J/kg.K) :"))
            E = m*c*t
            print("L'énergie échangé est de '= {:.2f} J".format(E))
        if chaleur == 2:
            m = float(input("Masse de l'échantillon (en kg) :"))
            delta_T = float(input("Différence de température (en °C) :"))
            E = float(input("Énergie échangée (en J) :"))
            c = E/(m*delta_T)
            print("La capacité thermique massique C = {:.2f} J/kg.K".format(Cp))
        elif chaleur == 3:
            c = float(input("Capacité thermique massique (en J/kg.K) :"))
            delta_T = float(input("Différence de température (en °C) :"))
            E = float(input("Énergie échangée (en J) :"))
            m = E/(c*delta_T)
            print("La masse de l'échantillon m = {:.2f} kg".format(m))
        elif chaleur == 4:
            c = float(input("Capacité thermique massique (en J/kg.K) :"))
            m = float(input("Masse de l'échantillon (en kg) :"))
            E = float(input("Énergie échangée (en J) :"))
            delta_T = E/(m*c)
            print("La différence de température ΔT = {:.2f} °C".format(delta_T))
    elif thermodynamique == 4:
        print("\n Quelle variable cherchez-vous ?")
        print("1. E (en J)")
        print("2. m (en kg)")
        print("3. L (en J/kg)")
        etat = float(input("Indiquez votre choix :"))
        if etat == 1:
            m = float(input("Masse de l'échantillon (en kg) :"))
            l = float(input("Energie massique de \n changement d'état (en J/kg) :"))
            E = m*l
            print("L'energie échangé est de ' = {:.2f} J".format(E))
        elif etat == 2:
            l = float(input("Energie massique de \n changement d'état (en J/kg) :"))
            E = float(input("Énergie échangée (en J) :"))
            m = E/l
            print("La masse est de m = {:.2f} kg".format(m))
        elif etat == 3:
            E = float(input("Énergie échangée (en J) :"))
            m = float(input("Masse de l'échantillon (en kg) :"))
            l = E/m
            print("L’énergie massique de \n changement d’état est de = {:.2f} J/kg".format(l))
        else:
            print("Choix invalide. Veuillez réessayer.")
    else:
        print("Choix invalide. Veuillez réessayer.")
elif groupe == 3:
    print("1. Force")
    print("2. Travail")
    print("3. Puissance")
    print("4. Vitesse instantanée")
    print("5. Compensation des forces")
    mecanique = float(input("Indiquez votre choix :"))
    if mecanique == 1:
        print("\n Quelle variable cherchez-vous ?")
        print("1. F (en N)")
        print("2. m (en kg)")
        print("3. a (en m/s²)")
        force = float(input("Indiquez votre choix :"))
        if force == 1:
            m = float(input("Masse de l'objet :"))
            a = float(input("Accélération de l'objet :"))
            F = m * a
            print("La force F = {:.2f} N".format(F))
        elif force == 2:
            F = float(input("Force appliquée sur l'objet :"))
            a = float(input("Accélération de l'objet :"))
            m = F / a
            print("La masse de l'objet est de {:.2f} kg".format(m))
        elif force == 3:
            F = float(input("Force appliquée sur l'objet :"))
            m = float(input("Masse de l'objet :"))
            a = F / m
            print("L'accélération de l'objet est de {:.2f} m/s²".format(a))
    elif mecanique == 2:
        print("\n Quelle variable cherchez-vous ?")
        print("1. W (en J)")
        print("2. F (en N)")
        print("3. d (en m)")
        print("4. α (en degrés)")
        travail = float(input("Indiquez votre choix :"))
        if travail == 1:
            F = float(input("Force appliquée sur l'objet :"))
            d = float(input("Distance parcourue par l'objet :"))
            alpha_angle = float(input("Angle α (en degrés) :"))
            angle_en_rad = math.radians(alpha_angle)
            cosinus = math.cos(angle_en_rad)
            W = F * d * cosinus
            print("Le travail W = {:.2f} J".format(W))
        elif travail == 2:
            W = float(input("Travail effectué sur l'objet :"))
            d = float(input("Distance parcourue par l'objet :"))
            alpha_angle = float(input("Angle α (en degrés) :"))
            angle_en_rad = math.radians(alpha_angle)
            cosinus = math.cos(angle_en_rad)
            F = W / d * cosinus
            print("La force appliquée sur l'objet est de {:.2f} N".format(F))
        elif travail == 3:
            W = float(input("Travail effectué sur l'objet :"))
            F = float(input("Force appliquée sur l'objet :"))
            alpha_angle = float(input("Angle α (en degrés) :"))
            angle_en_rad = math.radians(alpha_angle)
            cosinus = math.cos(angle_en_rad)
            d = W / F * cosinus
            print("La distance parcourue par l'objet est de {:.2f} m".format(d))
    elif mecanique == 3:
        print("\n Quelle variable cherchez-vous ?")
        print("1. P (en W)")
        print("2. C (en Nm)")
        print("3. Ꞷ (en rad/s)")
        puissance_couple = float(input("Indiquez votre choix :"))
        if puissance_couple == 1:
            C = float(input("Couple (en Nm):"))
            omega = float(input("Rotation (en rad/s) :"))
            P = C * omega
            print("La puissance P = {:.2f} W".format(P))
        elif puissance_couple == 2:
            P = float(input("Puissance (en W) :"))
            omega = float(input("Rotation (en rad/s) :"))
            C = P/omega
            print("Le couple est de  {:.2f} Nm")
        elif puissance_couple == 3:
            P = float(input("Puissance (en W) :"))
            C = float(input("Couple (en Nm):"))
            omega = P/C
            omega_tr = (omega*2*pi)/60
            print("La rotation est de {:.2f} rad/s".format(omega))
            print("La rotation est de {:.2f} tr/min".format(omega_tr))
    elif mecanique == 4:
        print("\n Quelle variable cherchez-vous ?")
        print("1. Vitesse de translation (en m/s)")
        print("2. Vitesse de rotation (en tr/min)")
        print("3. Diamètre (en m)")
        vitesse = float(input("Indiquez votre choix :"))
        if vitesse == 1:
            n = float(input("Rotation en tr/min :"))
            d = float(input("Diamètre de la roue :"))
            v = (pi*d*n)/60
            print("La vitesse de translation est de {:.2f} m/s".format(v))
        elif vitesse == 2:
            v = float(input("Vitesse de translation :"))
            d = float(input("Diamètre de la roue :"))
            n = (60*v)/(pi*d)
            n_rad = (n*2*pi)/60
            print("La rotation est de {:.2f} rad/s".format(n_rad))
            print("La rotation est de {:.2f} tr/min".format(n))
        elif vitesse == 3:
            n = float(input("Rotation en tr/min :"))
            v = float(input("Vitesse de translation :"))
            d = (60*v)/(pi*n)
            print("Le diamètre de la roue est de {:.2f} m".format(d))
    elif mecanique == 5:
        print("\n Quelle variable cherchez-vous ?")
        print("1. m (en kg)")
        print("2. v (en m/s)")
        print("3. S (en m²)")
        frottement = float(input("Indiquez votre choix :"))
        if frottement == 1:
            cx =float(input("Coéficient de trainée :"))
            p =float(input("Masse volumique du fluide (kg/m³) :"))
            s =float(input("Surface de référence (en m²) :"))
            v =float(input("Vitesse (em m/s) :"))
            m = (0.5*p*cx*s*(v**2))/g        
            print("\n La masse de l'objet est {:.2f} kg \n pour que les forces se compensent.".format(m))
        elif frottement == 2:
            cx =float(input("Coéficient de trainée :"))
            p = float(input("Masse volumique du fluide (kg/m³) :"))
            m = float(input("Masse (en kg) :"))
            s =float(input("Surface de référence (en m²) :"))
            v = math.sqrt((2*m*g)/p*cx*s)
            print("\n La vitesse est {:.2f} m/s \n lorsque les forces se compensent.".format(v))
        elif frottement == 3:
            cx =float(input("Coéficient de trainée :"))
            p = float(input("Masse volumique du fluide (kg/m³) :"))
            m = float(input("Masse (en kg) :"))
            v = float(input("Vitesse (em m/s) :"))
            s = (2*m*g)/(p*cx*(v**2))
            print("La surface est {:.2f} m/s \n pour que les forces se compensent.".format(s))
    else:
        print("Choix invalide. Veuillez réessayer.")
elif groupe == 4:
    print("1. Résistance équivalente")
    print("2. Puissance apparente")
    print("3. ")
    print("4. ")
    elec = int(input("Indiquez votre choix :"))
    if elec == 1:
        print("\n Quelle configuration cherchez-vous ?")
        print("1. En dérivation")
        print("2. En série")
        resistance = int(input("Indiquez votre choix :"))
        if resistance == 1:
            R1 = int(input("Valeur de R1 (en ohm): "))
            R2 = int(input("Valeur de R2 (en ohm): "))
            Re = (R1*R2)/(R1 + R2)
            print("\n La résistance équivalent vaut {:.2f} ohm.".format(Re))
        elif resistance == 2:
            R1 = int(input("Valeur de R1 (en ohm): "))
            R2 = int(input("Valeur de R2 (en ohm): "))
            Re = R1 + R2
            print("\n La résistance équivalent vaut {:.2f} ohm.".format(Re))
    elif elec == 2:
        print("\n Quelle variable cherchez-vous ?")
        print("1. Calcul de Ueff")
        print("2. Calcul de Ieff")
        print("3. Calcul de S")
        apparente = int(input("Indiquez votre choix :"))
        if == 1:
            u = float(input("Umax (en V) :"))
            ueff = u/(math.sqrt(2))
            print("La valeur de Ueff est de {:.2f} V".format(ueff))
        elif == 2:
            i = float(input("Imax (en A) :"))
            ieff = i/(math.sqrt(2))
            print("La valeur de Ieff est de {:.2f} A".format(ieff))
        elif  == 3:
            i = float(input("Ieff (en A) :"))
            u = float(input("Ueff (en V) :"))
            s = i*u
            print("La valeur de la puissance aparante est {:.2f} W".format(s))
            print(" {:.2f} ".format())
        elif  == 4:
            print(" {:.2f} ".format())
    elif elec == 3:
        print("\n Quelle variable cherchez-vous ?")
        print("1. ")
        print("2. ")
        print("3. ")
        print("4. ")
         = float(input("Indiquez votre choix :"))
        if == 1:
            print(" {:.2f} ".format())
        elif == 2:
            print(" {:.2f} ".format())
        elif  == 3:
            print(" {:.2f} ".format())
        elif  == 4:
            print(" {:.2f} ".format())
    elif elec == 4:
        print("\n Quelle variable cherchez-vous ?")
        print("1. ")
        print("2. ")
        print("3. ")
        print("4. ")
         = float(input("Indiquez votre choix :"))
        if == 1:
            print(" {:.2f} ".format())
        elif == 2:
            print(" {:.2f} ".format())
        elif  == 3:
            print(" {:.2f} ".format())
        elif  == 4:
            print(" {:.2f} ".format())
    else:
        print("Choix invalide. Veuillez réessayer.")
elif groupe == 5:
    print("1. Cube")
    print("2. Pyramide à base triangulaire")
    print("3. Pyramide à base carrée")
    print("4. Cylindre")
    print("5. Cône")
    print("6. Sphère")
    print("7. Pyramide à base rectangulaire")
    print("8. Prisme triangulaire")
    geometrie = float(input("Indiquez votre choix : "))
    if geometrie == 1:
        print("Quelle grandeur cherchez-vous ?")
        print("1. Aire de la base")
        print("2. Volume")
        choix = int(input("Indiquez votre choix : "))
        if choix == 1:
            c = float(input("Longueur de l'arête : "))
            b = c * c
            print("La surface de la base est de {:.2f} u²".format(b))
        elif choix == 2:
            c = float(input("Longueur de l'arête : "))
            v = c * c * c
            print("Le volume du cube est de {:.2f} u³".format(v))

    if geometrie == 2:
        print("Quelle grandeur cherchez-vous ?")
        print("1. Aire de la base")
        print("2. Volume")
        choix = int(input("Indiquez votre choix : "))
        if choix == 1:
            b = float(input("Longueur de la base : "))
            h = float(input("Hauteur de la pyramide : "))
            aire_base = 0.5 * b * h
            print("L'aire de la base de la pyramide est de {:.2f} u²".format(aire_base))
        elif choix == 2:
            b = float(input("Longueur de la base : "))
            h = float(input("Hauteur de la pyramide : "))
            volume = (1/3) * b * b * h
            print("Le volume de la pyramide à base triangulaire est de {:.2f} u³".format(volume))