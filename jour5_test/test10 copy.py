def est_eligible(age, statut):
    if age >= 18:
        if statut == "étudiant":
            return True
        elif statut == "actif":
            return False
    return False


def afficher_tarif(nom, age, statut="inconnu"):
    if est_eligible(age, statut):
        tarif = 10
        print(nom, ": Tarif réduit à", tarif, "€")
    elif age < 18:
        tarif = 5
        print(nom, ": Tarif enfant à", tarif, "€")
    else:
        tarif = 20
        print(nom, ": Tarif plein à", tarif, "€")


afficher_tarif("Léo", 22, "étudiant")
afficher_tarif("Maya", 15, "étudiant")
afficher_tarif("Luc", 30, "actif")
afficher_tarif("Emma", 25)