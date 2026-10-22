def my_sort(number_list):
    sorted_list = number_list.copy()
    swap = True
    count = 0

    while swap:
        swap = False

        for index in range(len(sorted_list) - 1):
            if sorted_list[index] > sorted_list[index + 1]:
                (sorted_list[index], sorted_list[index + 1]) = (sorted_list[index + 1], sorted_list[index]) 

                swap = True
                count += 1
         
    print(f"""\nNombre total de coups nécessaires pour trier la liste : {count}
Liste triée : {sorted_list}\n""")

number_list = [56, 26, -19, 6, -56, 9, 0]
my_sort(number_list)