class Rectangulo:
    def __init__(self, largo, ancho):
        # Inicializa el largo y el ancho del rectángulo.
        # Verifica que ambos valores sean mayores que cero.
        if largo <= 0 or ancho <= 0:
            raise ValueError("Largo y ancho deben ser mayores que cero.")
        self.__largo = largo
        self.__ancho = ancho

    def cambiar_dimensiones(self, largo, ancho):
        # Cambia las dimensiones del rectángulo.
        # Verifica que los nuevos valores sean mayores que cero.
        if largo <= 0 or ancho <= 0:
            raise ValueError("Largo y ancho deben ser mayores que cero.")
        self.__largo = largo
        self.__ancho = ancho

    def calcular_area(self):
        # Calcula el área del rectángulo.
        return self.__largo * self.__ancho

    def calcular_perimetro(self):
        # Calcula el perímetro del rectángulo.
        return 2 * (self.__largo + self.__ancho)

    def consultar_dimensiones(self):
        # Devuelve las dimensiones actuales del rectángulo como una tupla.
        return self.__largo, self.__ancho

if __name__ == "__main__":
    # Crear un rectángulo con largo 10 y ancho 5.
    rectangulo = Rectangulo(10, 5)

    # Consultar y mostrar las dimensiones iniciales.
    print("Dimensiones iniciales:", rectangulo.consultar_dimensiones())
    
    # Calcular y mostrar el área y el perímetro inicial.
    print("Área:", rectangulo.calcular_area())
    print("Perímetro:", rectangulo.calcular_perimetro())

    # Cambiar las dimensiones del rectángulo a largo 20 y ancho 10.
    rectangulo.cambiar_dimensiones(20, 10)

    # Consultar y mostrar las nuevas dimensiones.
    print("Nuevas dimensiones:", rectangulo.consultar_dimensiones())

    # Calcular y mostrar el área y el perímetro con las nuevas dimensiones.
    print("Área:", rectangulo.calcular_area())
    print("Perímetro:", rectangulo.calcular_perimetro())
