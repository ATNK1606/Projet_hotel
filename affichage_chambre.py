import os
from turtle import clearscreen

# Offres
offre_standard_ch_i = ['2 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_standard_ch_d = ['3 personnes', 'TV', 'Lit double 80 * 80','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_suite_royale = ['2 personnes', 'TV', 'Lit double 200 * 200','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches', 'Corbeille de fruits','Serveur dédié à la chambre', 'Pack de bienvenue']
offre_studio = ['3 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches','Canapé','Kitchenette']

# Disponibilités
disponibilites = {
    "STANDARD": {},
    "CHAMBRE DOUBLE": {},
    "SUITE ROYALE": {},
    "STUDIO": {}
}

# CLASSE CHAMBRE 
class Chambre:
    def __init__(self, nombre, prix, infos, nuit, heure):
        self.nombre = nombre
        self.prix = prix
        self.heure = heure
        self.nuit = nuit
        self.infos = infos

    def modifier_nombre(self, nouveau_nombre):
        if nouveau_nombre >= 0:
            self.nombre = nouveau_nombre
        else:
            print("Le nombre de chambres doit être positif.")

    def modifier_prix(self, nouveau_prix):
        if nouveau_prix >= 0:
            self.prix = nouveau_prix
        else:
            print("Le prix doit être positif.")

    def afficher_chambre(self):
        print(f"Nombre de chambres : {self.nombre}")

    def afficher_heure(self):
        print(f"Heure d'arrivée : {self.heure}")

    def afficher_prix(self):
        print(f"Prix : {self.prix} €")

    def afficher_nuits(self):
        print(f"Nuits : {self.nuit}")


# FONCTION POUR DEMANDER UN CHOIX NUMÉRIQUE
def demander_choix(prompt, min_val=None, max_val=None):
    while True:
        val = input(prompt)
        if val.isdigit():
            val = int(val)
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            else:
                return val
        else:
            print(f"'{val}' n'est pas un nombre. Veuillez entrer un entier.\n")


#  MENUS PRINCIPAUX 
def main():
    main_menu()

def main_menu():
    os.system('cls')
    print("--------------------------------------------------")
    print("     BIENVENUE DANS NOTRE APP DE RESERVATION      ")
    print("--------------------------------------------------")
    print("     1.VOIR NOS TOUTES LES OFFRES")
    print("     2.QUITTER")
    print("--------------------------------------------------")
    
    choix = demander_choix("Veuillez choisir une option : ", 1, 2)
    menu_offres(choix)


def menu_offres(choix):
    if choix == 1:
        clearscreen()
        print("--------------------------------------------------")
        print("VOICI LES OFFRES DISPONIBLES DANS NOTRE HOTEL")
        print("--------------------------------------------------")
        print("1.OFFRE STANDARD (CHAMBRE INDIVIDUELLE) | QUANTITÉ : 3")
        print("2.OFFRE STANDARD+ (CHAMBRE DOUBLE) | QUANTITÉ : 2")
        print("3.OFFRE SUITE ROYALE | QUANTITÉ : 3")
        print("4.OFFRE STUDIO | QUANTITÉ : 3")
        print("0.RETOUR")
        print("--------------------------------------------------")

        choix_offre = demander_choix("Veuillez choisir une offre : ")
        print("--------------------------------------------------")

        while choix_offre < 0 or choix_offre > 4:
            os.system('cls')
            print("L'option", choix_offre, "ne figure pas parmi les offres.")
            choix_offre = demander_choix("Veuillez choisir une offre : ")

        affichage_offre(choix_offre)


def affichage_offre(choix_offre):
    retour = 2  
    if choix_offre == 1:
        while retour < 0 or retour > 1:
            affichage_titre("STANDARD")
            affichage(offre_standard_ch_i)
            print("1.Reserver la chambre")
            print("0.Retour")
            print("--------------------------------------------------")
            retour = demander_choix("Veuillez choisir une option : ")
        if retour == 0:
            menu_offres(1)
        else:
            reservation("STANDARD", offre_standard_ch_i, 3)

    elif choix_offre == 2:
        while retour < 0 or retour > 1:
            affichage_titre("CHAMBRE DOUBLE")
            affichage(offre_standard_ch_d)
            print("1.Reserver la chambre")
            print("0.Retour")
            print("--------------------------------------------------")
            retour = demander_choix("Veuillez choisir une option : ")
        if retour == 0:
            menu_offres(1)
        else:
            reservation_d("CHAMBRE DOUBLE", offre_standard_ch_d, 2)

    elif choix_offre == 3:
        while retour < 0 or retour > 1:
            affichage_titre("SUITE ROYALE")
            affichage(offre_suite_royale)
            print("1.Reserver la chambre")
            print("0.Retour")
            print("--------------------------------------------------")
            retour = demander_choix("Veuillez choisir une option : ")
        if retour == 0:
            menu_offres(1)
        else:
            reservation_d("SUITE ROYALE", offre_suite_royale, 3)

    elif choix_offre == 4:
        while retour < 0 or retour > 1:
            affichage_titre("STUDIO")
            affichage(offre_studio)
            print("1.Reserver la chambre")
            print("0.Retour")
            print("--------------------------------------------------")
            retour = demander_choix("Veuillez choisir une option : ")
        if retour == 0:
            menu_offres(1)
        else:
            reservation("STUDIO", offre_studio, 3)
    else:
        os.system('cls')
        main_menu()


def affichage_titre(titre):
    os.system('cls')
    print("--------------------------------------------------")
    print("INFOS SUR L'OFFRE", titre)
    print("--------------------------------------------------")


def affichage(offre):
    for i in offre:
        print(i)
    print("--------------------------------------------------")


# RÉSERVATION 
def reservation(titre, type_, quantite):
    nombre = 4
    chambre = []
    while nombre > quantite or nombre <= 0:
        affichage_titre(titre)
        affichage(type_)
        print("Il y a", quantite, "chambres disponibles pour cette offre !")
        nombre = demander_choix("Veuillez saisir le nombre de chambre : ")

    # Demander la date d'arrivée
    date_arrivee = input("Veuillez saisir la date d'arrivée (JJ/MM/AAAA) : ")

    # Vérifier la disponibilité
    deja_reserve = disponibilites[titre].get(date_arrivee, 0)
    if deja_reserve + nombre > quantite:
        print("\n Désolé, il n’y a pas assez de chambres disponibles à cette date.")
        input("Appuyez sur Entrée pour revenir...")
        menu_offres(1)
        return

    for i in range(nombre):
        nuit = 0
        while nuit <= 0:
            affichage_titre(titre)
            affichage(type_)
            nuit = demander_choix("Veuillez choisir le nombre de nuits pour la chambre : ")
        print("Attention pour une heure d'arrivée hors 13h-17h une pénalité de 15 euros")
        heure = demander_choix("Veuillez saisir l'heure d'arrivée : ")
        prix = 18 * nuit if 13 <= heure <= 17 else (18 * nuit) + 15
        chambre.append(Chambre(nombre, prix, type_, nuit, heure))

    # Mise à jour des disponibilités
    disponibilites[titre][date_arrivee] = disponibilites[titre].get(date_arrivee, 0) + nombre

    affichage_reservation(chambre)


def reservation_d(titre, type_, quantite):
    nombre = 4
    chambre = []
    while nombre > quantite or nombre <= 0:
        affichage_titre(titre)
        affichage(type_)
        print("Il y a", quantite, "chambres disponibles pour cette offre !")
        nombre = demander_choix("Veuillez saisir le nombre de chambre : ")

    # Demander la date d'arrivée
    date_arrivee = input("Veuillez saisir la date d'arrivée (JJ/MM/AAAA) : ")

    # Vérifier la disponibilité
    deja_reserve = disponibilites[titre].get(date_arrivee, 0)
    if deja_reserve + nombre > quantite:
        print("\n Désolé, il n’y a pas assez de chambres disponibles à cette date.")
        input("Appuyez sur Entrée pour revenir...")
        menu_offres(1)
        return

    for i in range(nombre):
        nuit = 0
        while nuit < 2:
            affichage_titre(titre)
            affichage(type_)
            print("Pour l'offre :", titre, "Il faut reserver au minimum 2 nuits !")
            nuit = demander_choix("Veuillez choisir le nombre de nuits pour la chambre : ")
        print("Attention pour une heure d'arrivée hors 13h-17h une pénalité de 15 euros")
        heure = demander_choix("Veuillez saisir l'heure d'arrivée : ")
        prix = 18 * nuit if 13 <= heure <= 17 else (18 * nuit) + 15
        chambre.append(Chambre(nombre, prix, type_, nuit, heure))

    # Mise à jour des disponibilités
    disponibilites[titre][date_arrivee] = disponibilites[titre].get(date_arrivee, 0) + nombre

    affichage_reservation(chambre)


def affichage_reservation(chambre):
    choix = -1
    while choix < 0 or choix > 1:
        print("--------------------------------------------------")
        for i, ch in enumerate(chambre, 1):
            print(f"Facturation de la reservation {i}")
            ch.afficher_chambre()
            ch.afficher_prix()
            ch.afficher_nuits()
            ch.afficher_heure()
        print("--------------------------------------------------")
        print("1.Quitter")
        print("0.Retour")
        choix = demander_choix("Veuillez choisir une option : ")
    menu_offres(1)


main()
