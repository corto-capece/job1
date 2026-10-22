def get_type_saison(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "été":
            print("Poire, fraise, cassis")

    elif type == "légume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "été":
            print("artichaut, aubergine, navet")

get_type_saison("fruits", "hiver")
get_type_saison("fruits", "été")
get_type_saison("légume", "hiver")
get_type_saison("légume", "été")