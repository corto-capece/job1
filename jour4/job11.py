def time_to_text(nombre_entier):
    hours = nombre_entier // 60
    minutes = nombre_entier % 60

    print(f"{hours} heures et {minutes} minutes")

time_to_text(55)
time_to_text(555)
