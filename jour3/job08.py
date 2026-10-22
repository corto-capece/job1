side_a = int(input("Veuillez saisir une valeur (a) : "))
side_b = int(input("Veuillez saisir une valeur (b) : "))
side_c = int(input("Veuillez saisir une valeur (c) : "))

if (side_a + side_b <= side_c
    or side_a + side_c <= side_b
    or side_b + side_c <= side_a):
    print("Impossible de créer un triangle avec les longueurs choisies")

elif side_a == side_b == side_c:
    print("C'est un triangle équilatéral")

elif (side_a ** 2 + side_b ** 2 == side_c ** 2
    or side_a ** 2 + side_c ** 2 == side_b ** 2
    or side_b ** 2 + side_c ** 2 == side_a ** 2):

    if ((side_a == side_b) or (side_a == side_c) or (side_b == side_c)):
        print("C'est un triangle isocèle et rectangle")

    else:
        print("C'est un triangle rectangle")

elif ((side_a == side_b) or (side_a == side_c) or (side_b == side_c)):
    print("C'est un triangle isocèle")

else:
    print("C'est un triangle quelconque")
