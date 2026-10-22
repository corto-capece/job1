def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

user_note1 = int(input("Veuillez saisir la note 1 : "))
user_note2 = int(input("Veuillez saisir la note 2 : "))
user_note3 = int(input("Veuillez saisir la note 3 : "))

moyenne_etudiant = moyenne(user_note1, user_note2, user_note3)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")

elif moyenne_etudiant >= 11:
    print("Bon élève")

elif moyenne_etudiant >= 8:
    print("Élève moyen")

else:
    print("Élève devant faire des efforts")