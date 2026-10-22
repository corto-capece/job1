def round_grades(list_grades):
    new_list_grades = []
    for grade in list_grades:
        
        if grade >= 40 and grade % 5 >= 3:
            grade += (5 - (grade % 5))

        new_list_grades.append(grade)
                                
    return new_list_grades

list_grades = [39, 40, 41, 42, 43, 44, 45, 46]
print(round_grades(list_grades))