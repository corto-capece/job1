user_input = int(input("Entrez un entier supérieur à zéro (N) : "))
print(f"Table de multiplication de {user_input} : ")
for number in range(11):
    print(f"{user_input} x {number} = {user_input * number}")