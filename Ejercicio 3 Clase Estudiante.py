class Estudiante:
    def __init__(self, nombre, edad):
        # Inicializa el nombre, la edad y una lista para las notas del estudiante.
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []

    def agregar_nota(self, nota):
        # Agrega una nota al estudiante si está en el rango de 0 a 100.
        # Si la nota es inválida, muestra un mensaje de error.
        if 0 <= nota <= 100:
            self.__notas = self.__notas + [nota]  # Agrega la nota creando una nueva lista.
        else:
            print("Nota inválida: debe estar entre 0 y 100.")

    def calcular_promedio(self):
        # Calcula y devuelve el promedio de las notas.
        # Si no hay notas, devuelve 0.
        return sum(self.__notas) / len(self.__notas) if self.__notas else 0

    def consultar_nombre(self):
        # Devuelve el nombre del estudiante.
        return self.__nombre

    def consultar_edad(self):
        # Devuelve la edad del estudiante.
        return self.__edad

if __name__ == "__main__":
    # Crea un estudiante con un nombre y una edad inicial.
    estudiante = Estudiante("Juan Perez", 20)

    # Muestra el nombre y la edad del estudiante.
    print("Nombre:", estudiante.consultar_nombre())
    print("Edad:", estudiante.consultar_edad())

    # Agrega varias notas válidas al estudiante.
    estudiante.agregar_nota(100)
    estudiante.agregar_nota(100)
    estudiante.agregar_nota(100)

    # Calcula y muestra el promedio de las notas.
    print("Promedio de notas:", estudiante.calcular_promedio())

    
