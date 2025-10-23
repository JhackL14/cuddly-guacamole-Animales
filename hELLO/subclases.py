# animales.py
from Animales import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hablar(self):
        return "Guau guau"

    def info(self):
        return f"{super().info()} Es un perro de raza {self.raza}."


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hablar(self):
        return "Miau"

    def info(self):
        return f"{super().info()} Es un gato de color {self.color}."


class Pajaro(Animal):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre, edad)
        self.tipo = tipo

    def hablar(self):
        return "Pío pío"

    def volar(self):
        return f"{self.nombre} está volando."

    def info(self):
        return f"{super().info()} Es un pájaro del tipo {self.tipo}."