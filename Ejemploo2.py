def calcular(termino01, termino02, termino03):
    producto = termino01 * termino02 + termino03
    return producto

if __name__ == "__main__":
    termino01 = float(input("Ingrese termino 1: "))
    termino02 = float(input("Ingrese termino 2: "))
    termino03 = float(input("Ingrese termino 3: "))
    resultado = calcular(termino01, termino02, termino03)
    print(f"{termino01} * {termino02} + {termino03} = {resultado}")
