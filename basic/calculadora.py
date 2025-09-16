# Calculadora básica usando match, pide dos números y una operación(suma, resta, multiplicación, división) y calcula el resultado.

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (suma, resta, multiplicacion, division): ").lower()

match operacion:
    case "suma":
        print(f"Resultado: {a + b}")
    case "resta":
        print(f"Resultado: {a - b}")
    case "multiplicacion":
        print(f"Resultado: {a * b}")
    case "division":
        if b != 0:
            print(f"Resultado: {a / b}")
        else:
            print("Error: No se puede dividir entre 0")
    case _:
        print("Operación no válida, usa: suma, resta, multiplicacion o division")                       