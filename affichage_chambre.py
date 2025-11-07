import os

# Offres
offre_standard_ch_i = ['2 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_standard_ch_d = ['3 personnes', 'TV', 'Lit double 80 * 80','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches']
offre_suite_royale = ['2 personnes', 'TV', 'Lit double 200 * 200','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches', 'Corbeille de fruits','Serveur dédié à la chambre', 'Pack de bienvenue']
offre_studio = ['3 personnes', 'TV', 'Lit double 140 * 120','Petit frigo', 'Machine à café', 'Set de thé','Set de bain','3 serviettes de douches','Canapé','Kitchenette']

# Fonction pour nettoyer l'écran
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour demander un choix numérique sécurisé
def demander_choix(prompt, min_val, max_val):
    while True:
        val = input(prompt)
        if val.isdigit():
            val = int(val)
            if min_val <= val <= max_val:
                return val
            else:
                print(f"L'option {val} n'est pas dans la plage {min_val}-{max_val}.")
        else:
            print(f"'{val}' n'est pas un nombre. Veuilez entrer un entier.")

# Affichage des titres
def affichage_titre(titre):
    clear_screen()
    print("--------------------------------------------------")
    print("INFOS SUR L'OFFRE ", titre)
    print("--------------------------------------------------")

# Affichage d'une offre
def affichage(offre):
    for i in offre:
        print(i)
    print("--------------------------------------------------")

# Menu principal
def main_menu():
    clear_screen()
    print("--------------------------------------------------")
    print("     BIENVENUE DANS NOTRE APP DE RESERVATION      ")
    print("--------------------------------------------------")
    print("     1.VOIR NOS TOUTES LES OFFRES")
    print("     2.QUITTER")
    print("--------------------------------------------------")
    
    choix = demander_choix("Veuillez choisir une option : ", 1, 2)
    menu_offres(choix)

# Menu des offres
def menu_offres(choix):
    if choix == 1:
        clear_screen()
        print("--------------------------------------------------")
        print("VOICI LES OFFRES DISPONIBLES DANS NOTRE HOTEL")
        print("--------------------------------------------------")
        print("1.OFFRE STANDARD (CHAMBRE INDIVIDUELLE) | QUANTITÉ : 3")
        print("2.OFFRE STANDARD+ (CHAMBRE DOUBLE) | QUANTITÉ : 2")
        print("3.OFFRE SUITE ROYALE | QUANTITÉ : 3")
        print("4.OFFRE STUDIO | QUANTITÉ : 3")
        print("0.RETOUR")
        print("--------------------------------------------------")
        
        choix_offre = demander_choix("Veuillez choisir une offre : ", 0, 4)
        if choix_offre == 0:
            main_menu()
        else:
            affichage_offre(choix_offre)
    else:
        clear_screen()
        print("Merci d'avoir utilisé notre application. À bientôt !")
        exit()

# Affichage d'une offre spécifique
def affichage_offre(choix_offre):
    retour = 1
    while retour != 0:
        if choix_offre == 1:
            affichage_titre("STANDARD")
            affichage(offre_standard_ch_i)
        elif choix_offre == 2:
            affichage_titre("CHAMBRE DOUBLE")
            affichage(offre_standard_ch_d)
        elif choix_offre == 3:
            affichage_titre("SUITE ROYALE")
            affichage(offre_suite_royale)
        elif choix_offre == 4:
            affichage_titre("STUDIO")
            affichage(offre_studio)
        print("0.Retour")
        print("--------------------------------------------------")
        retour = demander_choix("Veuillez choisir une option : ", 0, 0)  # Seul 0 est valide pour revenir
    main_menu()

# Fonction principale
def main():
    main_menu()

# Lancement de l'application
if __name__ == "__main__":
    main()
