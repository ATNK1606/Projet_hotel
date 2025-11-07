offre_standard_ch_i = ['2 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_standard_ch_d = ['3 personnes', 'TV', 'Lit double 80 * 80','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_suite_royale = ['2 personnes', 'TV', 'Lit double 200 * 200','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches', 'Corbeille de fruits','Serveur dédié à la chambre', 'Pack de bienvenue'] #a faire le dernier
offre_studio = ['3 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches','Canapé','Kitchenette']
import os 
class Chambre:
    def __init__(self, nombre, prix,infos,nuit,heure):
        self.nombre = nombre
        self.prix = prix
       # self.date_debut  = date_debut
       #self.date_fin = date_fin
        self.heure = heure
        self.nuit = nuit
        self.infos = infos

    # Méthode pour modifier le nombre de chambres
    def modifier_nombre(self, nouveau_nombre):
        if nouveau_nombre >= 0:
            self.nombre = nouveau_nombre
        else:
            print("Le nombre de chambres doit être positif.")

    # Méthode pour modifier le prix de la chambre
    def modifier_prix(self, nouveau_prix):
        if nouveau_prix >= 0:
            self.prix = nouveau_prix
        else:
            print("Le prix doit être positif.")
    # Méthode pour afficher les informations de la chambre
    def afficher_chambre(self):
        print(f"Nombre de chambres : {self.nombre}")
    def afficher_heure(self):
        print(f"Heure d'arrivée : {self.heure}")
    def afficher_prix(self):
        print(f"Prix : {self.prix} €")
    def afficher_nuits(self):
        print(f"Nuits : {self.nuit} ")


def main() : 
   main_menu()
    
def main_menu ():
    os.system('cls')
    print("--------------------------------------------------")
    print("     BIENVENUE DANS NOTRE APP DE RESERVATION      ")
    print("--------------------------------------------------")
    print("     1.VOIR NOS TOUTES LES OFFRES")
    print("     2.QUITTER")
    print("--------------------------------------------------")
    choix = int(input("Veuillez choisir une option : "))
    print("--------------------------------------------------")
    while (choix < 1 or choix > 2) :
        os.system('cls')
        print("--------------------------------------------------")
        print("     BIENVENUE DANS NOTRE APP DE RESERVATION      ")
        print("--------------------------------------------------")
        print("     1.VOIR NOS TOUTES LES OFFRES")
        print("     2.QUITTER")
        print("--------------------------------------------------")
        print("L'option", choix," ne figure pas parmi les options")
        choix = int(input("Veuillez choisir une option : "))
        print("--------------------------------------------------")
    menu_offres(choix)


def menu_offres(choix) : 
    os.system('cls')
    if choix == 1 :
        os.system('cls')
        print("--------------------------------------------------")
        print("VOICI LES OFFRES DISPONIBLES DANS NOTRE HOTEL")
        print("--------------------------------------------------")
        print("1.OFFRE STANDARD (CHAMBRE INDIVIDUELLE) | QUANTITÉ : 3")
        print("2.OFFRE STANDARD+ (CHAMBRE DOUBLE) | QUANTITÉ : 2")
        print("3.OFFRE SUITE ROYALE | QUANTITÉ : 3")
        print("4.OFFRE STUDIO | QUANTITÉ : 3")
        print("0.RETOUR")
        print("--------------------------------------------------")
        choix_offre = int(input("Veuillez choisir une offre : "))
        print("--------------------------------------------------")
        while choix_offre < 0 or choix_offre > 4 :
            os.system('cls')
            print("--------------------------------------------------")
            print("VOICI LES OFFRES DISPONIBLES DANS NOTRE HOTEL")
            print("--------------------------------------------------")
            print("1.OFFRE STANDARD (CHAMBRE INDIVIDUELLE) | QUANTITÉ : 3")
            print("2.OFFRE STANDARD+ (CHAMBRE DOUBLE) | QUANTITÉ : 2")
            print("3.OFFRE SUITE ROYALE | QUANTITÉ : 3")
            print("4.OFFRE STUDIO | QUANTITÉ : 2")
            print("0.RETOUR")
            print("--------------------------------------------------")
            print("L'option", choix_offre," ne figure pas parmi les offres")
            choix_offre = int(input("Veuillez choisir une offre : "))
            print("--------------------------------------------------")
        affichage_offre(choix_offre)
    

def affichage_offre(choix_offre) : 
    retour = 2  
    if choix_offre == 1 :
        while retour < 0 or retour > 1 : 
            affichage_titre("STANDARD")
            affichage(offre_standard_ch_i)
            print("1.Reserver la chambre")
            print("0.Retour")
            print("--------------------------------------------------")
            retour = int(input("Veuillez choisir une option : "))
            print("--------------------------------------------------")
        if retour == 0 :
            menu_offres(1)
        elif retour == 1 : 
            reservation("STANDARD",offre_standard_ch_i,3)
                
    elif choix_offre == 2 : 
        while retour < 0 or retour > 1 :   
            affichage_titre("CHAMBRE DOUBLE")
            affichage(offre_standard_ch_i)
            print("1.Reserver la chambre")
            print("0.Retour")
            print("--------------------------------------------------")
            retour = int(input("Veuillez choisir une option : ")) 
            print("--------------------------------------------------")
        if retour == 0 :
            menu_offres(1)
        elif retour == 1 : 
            reservation_d("CHAMBRE DOUBLE",offre_standard_ch_i,2) ##################
    elif choix_offre == 3 :
        while retour < 0 or retour > 1 :   
            affichage_titre("SUITE ROYALE")
            affichage(offre_suite_royale)
            print("1.Reserver la chambre")
            print("0.Retour")
            print("--------------------------------------------------")
            retour = int(input("Veuillez choisir une option : "))
            print("--------------------------------------------------")
        if retour == 0 :
            menu_offres(1)
        elif retour == 1 : 
            reservation_d("SUITE ROYALE",offre_suite_royale,3) ##################
    elif choix_offre == 4 : 
        while retour < 0 or retour > 1 :  
            affichage_titre("STUDIO")
            affichage(offre_studio)
            print("1.Reserver la chambre")
            print("0.Retour")
            print("--------------------------------------------------")
            retour = int(input("Veuillez choisir une option : "))
            print("--------------------------------------------------")
        if retour == 0 :
            menu_offres(1)
        elif retour == 1 : 
            reservation("STUDIO",offre_studio,3) ##################
    else : 
        os.system('cls')
        main_menu()
def affichage_titre(titre):
    os.system('cls')
    print("--------------------------------------------------")
    print("INFOS SUR L'OFFRE ",titre)
    print("--------------------------------------------------")
def affichage (offre) :
    for i in offre: 
        print(i)
    print("--------------------------------------------------") 

def reservation (titre, type_, quantite) : 
    nombre = 4
    chambre = []
    while nombre > quantite or nombre <= 0 :
        affichage_titre(titre)
        affichage(type_)
        print("Il y a ", quantite," chambres disponibles pour cette offre !" )
        nombre = int(input("Veuillez saisir le nombre de chambre : "))
    for i in range(nombre) : 
        nuit = 0
        while nuit <= 0 : 
            affichage_titre(titre)
            affichage(type_)
            nuit = int(input("Veuillez choisir le nombre de nuits pour la chambre : "))
        print("Attention pour une heure d'arrivée hors 13h-17h une pénalité de 15 euros ")
        heure=int(input("Veuillez saisir l'heure d'arrivée : "))
        if heure  >= 13 and heure <= 17 : 
            prix  = 18 * nuit 
        else : 
            prix = (18 * nuit ) + 15 ###
        chambre.append(Chambre(nombre,prix,type_,nuit,heure)) ## a verifier
    affichage_reservation(chambre)

def reservation_d (titre, type_, quantite) : 
    nombre = 4
    chambre = []
    while nombre > quantite or nombre < 0 :
        affichage_titre(titre)
        affichage(type_)
        print("Il y a ", quantite," chambres disponibles pour cette offre !" )
        nombre = int(input("Veuillez saisir le nombre de chambre : "))
    for i in range(nombre) : 
        nuit = 0
        while nuit < 2 : 
            affichage_titre(titre)
            affichage(type_)
            print("Pour l'offre : ",titre," Il faut reserver au minimum 2 nuits !" )
            nuit = int(input("Veuillez choisir le nombre de nuits pour la chambre : "))
        print("Attention pour une heure d'arrivée hors 13h-17h une pénalité de 15 euros ")
        heure=int(input("Veuillez saisir l'heure d'arrivée : "))
        if heure  >= 13 and heure <= 17 : 
            prix  = 18 * nuit 
        else : 
            prix = (18 * nuit ) + 15 ###
        chambre.append(Chambre(nombre,prix,type_,nuit,heure)) ## a verifier
    affichage_reservation(chambre)

def affichage_reservation (chambre) : 
    choix = -1
    while choix < 0 or choix > 1 : 
        print("--------------------------------------------------")
        for i in range(len(chambre)) : 
            print("Facturation de la reservation",(i+1))
            chambre[i].afficher_chambre()
            chambre[i].afficher_prix()
            chambre[i].afficher_nuits()
            chambre[i].afficher_heure()
        print("--------------------------------------------------")
        print("1.Quitter")
        print("0.Retour")
        choix = int(input("Veuillez choisir une option : "))
        print("--------------------------------------------------")
    if choix == 0 : 
        menu_offres(1)
    elif choix == 1 : 
        menu_offres(1)
    



main()

