def test05():
    temperature = 22
    raining = False

    if temperature > 20 and not raining:
        print("Let's go outside!")
    elif temperature > 20 and raining:
        print("It’s raining.")
    else:
        print("Too cold.")


raining = True
test05()