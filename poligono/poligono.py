### Área de un Polígono ###
## Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

poligono = input("Introduce el polígono que quieras calcular: (triangulo, cuadrado, rectangulo)").lower()

match poligono:
    case "triangulo":

        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")

    case "cuadrado":

        lado = float(input("Introduce el lado del cuadrado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")

    case "rectangulo":        
        base = float(input("Introduce el lado del cuadrado: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        area = base * altura
        print(f"El área del rectángulo es: {area}")

    case _:
        print("Polígono no reconocido, prueba con triangulo, cuadrado o rectangulo.")   




