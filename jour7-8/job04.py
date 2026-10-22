import string

alphabet = string.ascii_lowercase

def make_secret(message, number):
    new_message = ""

    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + number) % len(alphabet)
            new_message += alphabet[new_index]

        else:
            new_message += letter
             
    return new_message

text = "avez-vous réussi à lire ce code secret ?"
print(make_secret(text, 3))
