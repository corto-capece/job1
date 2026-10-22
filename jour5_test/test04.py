def test04():
    score = 100

    if score >= 90:
        score -= 40
        print("Excellent!")
    elif score >= 60:
        score = 30
        print("Good job!")
    else:
        print("Try again!")

    print("Score:", score)


test04()