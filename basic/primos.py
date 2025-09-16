# Pide un número e indica si es primo o no.

a = int(input("Introduce un número: "))

if a <= 1:
    print(f"{a} no es primo")
else:
    es_primo = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{a} es primo")
    else:
        print(f"{a} no es primo")