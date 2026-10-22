def calculate_distance(number_scale, height_scale):
    distance = (2 * (number_scale * height_scale)) / 100
    total_distance = distance * 35

    print(f"Pour {number_scale} marches de {height_scale} cm, le gardien parcourt {total_distance:.2f} m par semaine.")

calculate_distance(1994, 21)
    
