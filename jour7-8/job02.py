def draw_triangle(height):
    for i in range(1, height):
        print(" " * (height - i) + "/" + " " * ((i * 2) - 2) + "\\")

    print("/" + "_" * ((height * 2) - 2) + "\\")

draw_triangle(5)