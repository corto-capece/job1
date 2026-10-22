amount = 10000
rate = 0.05

print("Gain annuel :", amount * rate)

amount2 = amount + 5000
rate2 = rate + 0.02

print("Nouveau gain annuel :", amount2 * rate2)

amount3 = amount2 - (amount2 * 0.1)
rate3 = rate2 - 0.01

print("Montant final de l'investissement :", amount3)
print("Gain annuel final :", amount3 * rate3)