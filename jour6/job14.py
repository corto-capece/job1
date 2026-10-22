def my_long_word(number, text):
    sorted_text = []
    
    for word in text.split():
        word = word.strip(",")
        length = 0

        for letter in word:
            length += 1

        if length > number:
            sorted_text.append(word)

    return sorted_text



text = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

print(my_long_word(3, text))

