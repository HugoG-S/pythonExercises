# Muetra la tabla de multiplicar de un número del 1 al 10

a = int(input("Introduce un número para saber su tabla de multiplicar: "))
print(f"La tabla de multiplicar de {a} es:")
for i in range (1, 11):
    print(f"{a} x {i} = {a * i}")