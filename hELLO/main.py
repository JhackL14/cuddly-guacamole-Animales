# main.py
from subclases import Perro, Gato, Pajaro
from firebase_class import FB   # Usa tu clase existente
import time

def subir_animales(fb, animales):
    """Sube una lista de animales a la base de datos en la nube."""
    for animal in animales:
        ref_user = fb.users_ref.child(animal.nombre)
        ref_user.set({
            'Nombre': animal.nombre,
            'Edad': animal.edad,
            'Tipo': animal.__class__.__name__,
            'Info': animal.info(),
            'Sonido': animal.hablar()
        })
        print(f"✅ Animal '{animal.nombre}' subido correctamente.")
        time.sleep(0.3)  # pequeña pausa visual (opcional)


def leer_animales(fb):
    """Lee todos los animales almacenados en la nube y los muestra."""
    ref = fb.users_ref
    data = ref.get()

    if not data:
        print("⚠️ No hay animales guardados en la nube.")
        return

    print("\n=== Información obtenida desde la nube ===\n")
    for nombre, info in data.items():
        print(f"🐾 {nombre}:")
        for clave, valor in info.items():
            print(f"   {clave}: {valor}")
        print("-" * 40)


def main():
    # Inicializar conexión con Firebase
    fb = FB()

    # Crear animales localmente
    perro = Perro("Rex", 5, "Labrador")
    gato = Gato("Michi", 3, "Naranja")
    pajaro = Pajaro("Piolín", 1, "Canario")

    animales = [perro, gato, pajaro]

    print("=== Subiendo animales a la nube ===")
    subir_animales(fb, animales)

    print("\nEsperando un momento antes de leer...\n")
    time.sleep(1)

    # Leer desde la nube
    leer_animales(fb)


if __name__ == "__main__":
    main()
