def calcule(num1, operator, num2):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2

print(calcule(6, "+", 3))
print(calcule(6, "-", 3))
print(calcule(6, "*", 3))
print(calcule(6, "/", 3))
print(calcule(6, "%", 3))