def main():
    # Aquí pedimos la cantidad de números que queremos meter en el array :)
    n = int(input("¿Cuántos números deseas ingresar? "))

    # en esta parte se crea la lista de números
    numeros = []
    for i in range(n):
        num = int(input("Ingresa un número: "))
        numeros.append(num)

    # Pedimos valor de k
    k = int(input("Ingresa el valor de k: "))

    # HashSet
    vistos = set()
    encontrado = False

    # Recorrer cada uno de los numeros
    for actual in numeros:
        complemento = k - actual

        # Ver si ya existe un par
        if complemento in vistos:
            print(f"Par encontrado: {complemento} + {actual} = {k}")
            encontrado = True

        # Agregar actual al conjunto
        vistos.add(actual)

    # Si no encontró ningún par
    if not encontrado:
        print(f"No existe ningún par que sume {k}")


if __name__ == "__main__":
    main()