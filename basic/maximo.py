# Solicita tres números y muestra cuál es el mayor.

numOne = float(input("Introduce un número: "))
numTwo = float(input("Introduce un segundo número: "))
numThree = float(input("Introduce un tercer y último número: "))

if numOne >= numTwo and numOne >= numThree:
    print(f"{numOne} es el mayor.")
elif numTwo >= numOne and numTwo >= numThree:
    print(f"{numTwo} es el mayor.")    
else:
    print(f"{numThree} es el mayor.")

## Alternativa usando max

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

print(f"El mayor es: {max(a, b, c)}")