def draw_table(n):
    middle_dash = "-" * (n + 1)

    print(f"+{middle_dash}+")

    for i in range(n + 1):
        line = list("#" * (n + 1))
        index = (n + 1) - (i + 1)
        line[index] = " "
        new_line = "".join(line)

        print(f"|{new_line}|")

    print(f"+{middle_dash}+")

draw_table(10)