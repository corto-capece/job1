def number_is_fair(number):
    if (type(number) is int) and number > 0:

        if number % 2 == 0:
            print("Pair")

        else:
            print("Impair")

    else:
        print("Veuillez saisir un nombre entier et positif")

number_is_fair(8)
number_is_fair(9)
number_is_fair(-10)
number_is_fair(10.5)
