class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        return "El animal hace un sonido genérico."

    def moverse(self):
        return f"{self.nombre} se mueve."

    def info(self):
        return f"{self.nombre} tiene {self.edad} años."