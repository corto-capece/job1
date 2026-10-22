def calculer_bonus(score, multiplicateur=2):
    bonus = score * multiplicateur
    return bonus


def traiter_joueur(nom, score):
    
    if score > 50:
        total = calculer_bonus(score)
        print(nom, "a un bonus de", total)
    else:
        total = calculer_bonus(score, 3)
        print(nom, "a un bonus réduit de", total)


score = 40
traiter_joueur("Alice", 60)
traiter_joueur("Bob", score)
print("Score final :", score)