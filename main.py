from subclases import Perro, Gato, Pajaro

def main():
    # Crear instancias de animales
    perro = Perro("azerbaiyan", 5, "Labrador")
    gato = Gato("#CC5500", 3, "Negro")
    pajaro = Pajaro("Muejejeje", 1, "Canario")

    # Lista con todos los animales
    animales = [perro, gato, pajaro]

    print("=== Información de los animales ===\n")

    # Mostrar información detallada de cada uno
    for animal in animales:
        print(animal.info())
        print("Habla:", animal.hablar())
        print("Movimiento:", animal.moverse())
        if hasattr(animal, "volar"):
            print("Acción especial:", animal.volar())
        print("-" * 40)

if __name__ == "__main__":
    main()