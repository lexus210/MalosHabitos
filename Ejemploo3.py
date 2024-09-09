# Función para calcular el área de un rectángulo
def arearectangulo(baser, alturar):
    area1 = baser * alturar
    return area1


# Función para calcular el área de un triángulo3
def areatriangulo(baset, alturat):
    area2 = 0.5 * baset * alturat
    return area2


if __name__ == "__main__":
    print("--- AREA RECTANGULO ---")
    baser = float(input("Ingrese la base del rectangulo: "))
    alturar = float(input("Ingrese la altura del rectangulo: "))
    area1 = arearectangulo(baser, alturar)
    print(f"El area del rectangulo es: {area1}")
    print("\n--- AREA TRIANGULO ---")
    baset = float(input("Ingrese la base del triangulo: "))
    alturat = float(input("Ingrese la altura del triangulo: "))
    area2 = areatriangulo(baset, alturat)
    print(f"El area del triangulo es: {area2}")
