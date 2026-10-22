def get_langage(langage):
    match langage:
        case "JavaScript":
            print("tu es un développeur web")
        case "python":
            print("tu es un développeur IA")
        case "java":
            print("tu es un développeur logiciel")
        case "reactjs":
            print("tu es un développeur mobile")
        case _:
            print("un jour, je serai le meilleur développeur...")

get_langage("JavaScript")
get_langage("python")
get_langage("java")
get_langage("reactjs")
get_langage("français")
