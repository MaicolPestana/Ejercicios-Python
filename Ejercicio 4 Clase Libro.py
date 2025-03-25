class Libro:
    def __init__(self, titulo, autor, paginas):
        # Inicializa los atributos del libro.
        if paginas <= 0:
            raise ValueError("El número de páginas debe ser mayor que cero.")
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas
        self.__pagina_actual = 1

    def avanzar_paginas(self, paginas):
        # Avanza páginas sin exceder el total, validando que el número de páginas sea positivo.
        if paginas < 0:
            raise ValueError("El número de páginas a avanzar debe ser positivo.")
        self.__pagina_actual = min(self.__pagina_actual + paginas, self.__paginas)

    def retroceder_paginas(self, paginas):
        # Retrocede páginas sin ir más allá de la página 1, validando que el número sea positivo.
        if paginas < 0:
            raise ValueError("El número de páginas a retroceder debe ser positivo.")
        self.__pagina_actual = max(self.__pagina_actual - paginas, 1)

    def consultar_pagina_actual(self):
        # Devuelve la página actual.
        return self.__pagina_actual

    def informacion_libro(self):
        # Devuelve información del libro.
        return f"Título: {self.__titulo}, Autor: {self.__autor}, Páginas: {self.__paginas}, Página actual: {self.__pagina_actual}"

if __name__ == "__main__":
    # Crea un libro y muestra su información.
    libro = Libro("El Quijote", "Miguel de Cervantes", 500)
    print(libro.informacion_libro())

    # Avanza y retrocede páginas mostrando resultados.
    libro.avanzar_paginas(20)
    print("Página actual:", libro.consultar_pagina_actual())
    libro.retroceder_paginas(40)
    print("Página actual:", libro.consultar_pagina_actual())

    # Ejemplo de error al avanzar con un número negativo.
    # libro.avanzar_paginas(-10)
