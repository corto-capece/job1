def test11(x, y, i):

    """
    Voici un commentaire appelé docstring. Il est utilisé pour documenter une fonction.
    
    Ceci est ma fonction test11

    Elle prend en paramètre:
        x: la taille
        y: la longueur
        i: l'index
    """

    if ((x > 5 and (y < 10 or i == 3)) or ((x < 0 or y == 7) and not (i > 10))) and not (x == y and i != 0):
        print(1)
    elif ((x <= 5 
           and (y > 10 and not (i == 2))) 
           or (x % 2 == 0 and (y % 3 == 0 or i == 0))):
        print("2")
    elif ((x + y + i) % 2 == 0 and not (x < y and y < i)):
        print(3)
    else:
        print('4')


test11(6, 5, 3)
test11(2, 9, 0)
test11(-1, 7, 5)
test11(4, 12, 2)
test11(1, 2, 3)







# Base d'utilisateurs : nom -> solde
utilisateurs = {
    "alice": 120.0,
    "bob": 75.5,
    "charles": 200.0
}

# --- Connexion ---
nom = input("Nom utilisateur : ").lower()

if nom not in utilisateurs:
    print("Utilisateur inconnu. Fin du programme.")
    exit()

solde = utilisateurs[nom]
choix = 0

print(f"Connecté en tant que {nom}. Solde initial : {solde} €")

# --- Menu principal ---
while choix != 4:
    print("\n1 - Voir le solde")
    print("2 - Déposer de l'argent")
    print("3 - Retirer de l'argent")
    print("4 - Quitter")

    choix = int(input("Votre choix : "))

    if choix == 1:
        print("Solde actuel :", solde, "€")

    elif choix == 2:
        montant = float(input("Montant à déposer : "))
        solde += montant
        print("Nouveau solde :", solde, "€")

    elif choix == 3:
        montant = float(input("Montant à retirer : "))
        if montant > solde:
            print("Solde insuffisant !")
        else:
            solde -= montant
            print("Nouveau solde :", solde, "€")

    elif choix == 4:
        print("Déconnexion...")
    else:
        print("Choix invalide.")

# Mise à jour du solde après déconnexion
utilisateurs[nom] = solde
print("Solde enregistré :", utilisateurs[nom], "€")