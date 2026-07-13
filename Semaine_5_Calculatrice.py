# Semaine 5 : Projet Calculatrice

def addition (a, b):
    return a + b

def soustration (a, b):
    return a - b

def multiplication (a, b):
    return a * b

def division (a, b):
    if b == 0:
        return "Erreur ou Impossible : division par zero"
    return a / b

print("Addition")
print("Soustraction")
print("Multiplication")
print("Division")
print()

# Programme

while True:
    print("\n=== CALCULATRICE ===")
    a = float(input("premier nombre :"))
    b = float(input("Deuxieme nombre :"))
    operation = input("Choisissez un signe (+, -, *, /)")

    if operation == "+":
        print("resultat :", addition(a, b))
    elif operation == "-":
        print("resultat :", soustration(a, b))
    elif operation == "*":
        print("reesultat :", multiplication(a, b))
    elif operation == "/":
        print("resultat :", division(a, b))
    else:
        print("Operation invalide.")