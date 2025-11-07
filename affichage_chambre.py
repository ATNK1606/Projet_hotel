offre_standard_ch_i = ['2 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_standard_ch_d = ['3 personnes', 'TV', 'Lit double 80 * 80','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_suite_royale = ['2 personnes', 'TV', 'Lit double 200 * 200','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches', 'Corbeille de fruits','Serveur dédié à la chambre', 'Pack de bienvenue'] #a faire le dernier
offre_studio = ['3 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches','Canapé','Kitchenette']
import os 
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
    retour = 1
    if choix_offre == 1 :
        while retour != 0 : 
            affichage_titre("STANDARD")
            affichage(offre_standard_ch_i)
            print("0.Retour")
            print("--------------------------------------------------")
            retour = int(input("Veuillez choisir une option : "))
            print("--------------------------------------------------")
        if retour == 0 :
            menu_offres(1)
    elif choix_offre == 2 : 
        while retour != 0 : 
            affichage_titre("CHAMBRE DOUBLE")
            affichage(offre_standard_ch_i)
            print("0.Retour")
            print("--------------------------------------------------")
            retour = int(input("Veuillez choisir une option : ")) 
            print("--------------------------------------------------")
        if retour == 0 :
            menu_offres(1)
    elif choix_offre == 3 :
        while retour != 0 : 
            affichage_titre("SUITE ROYALE")
            affichage(offre_suite_royale)
            print("0.Retour")
            print("--------------------------------------------------")
            retour = int(input("Veuillez choisir une option : "))
            print("--------------------------------------------------")
        if retour == 0 :
            menu_offres(1)
    elif choix_offre == 4 : 
        while retour != 0 :
            affichage_titre("STUDIO")
            affichage(offre_studio)
            print("0.Retour")
            print("--------------------------------------------------")
            retour = int(input("Veuillez choisir une option : "))
            print("--------------------------------------------------")
        if retour == 0 :
            menu_offres(1)
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


main()

