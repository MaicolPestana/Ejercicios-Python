class Producto:
    def __init__(self, nombre, precio):
        # Inicializa el nombre y el precio, asegurando que el precio sea mayor que cero.
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__nombre = nombre
        self.__precio = precio

    def cambiar_precio(self, nuevo_precio):
        # Cambia el precio si es mayor que cero.
        if nuevo_precio <= 0:
            raise ValueError("El nuevo precio debe ser mayor que cero.")
        self.__precio = nuevo_precio

    def consultar_precio(self):
        # Devuelve el precio actual.
        return self.__precio

    def obtener_nombre(self):
        # Devuelve el nombre del producto.
        return self.__nombre

    def aplicar_descuento(self, porcentaje_descuento):
        # Aplica un descuento si el porcentaje está entre 0 y 100.
        if not (0 <= porcentaje_descuento <= 100):
            raise ValueError("El descuento debe estar entre 0 y 100.")
        self.__precio -= self.__precio * (porcentaje_descuento / 100)

# Ejemplo de uso
if __name__ == "__main__":
    producto = Producto("Laptop", 1500)
    print("Producto:", producto.obtener_nombre())
    print("Precio inicial:", producto.consultar_precio())

    producto.cambiar_precio(1200)
    print("Nuevo precio:", producto.consultar_precio())

    producto.aplicar_descuento(20)
    print("Precio con descuento:", producto.consultar_precio())

