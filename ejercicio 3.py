class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializa los atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        # Verifica si hay suficiente stock para la cantidad solicitada
        return self.stock >= cantidad

    def vender(self, cantidad):
        # Vende una cantidad si hay suficiente stock
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")
        else:
            print(f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}.")

    def reabastecer(self, cantidad):
        # Incrementa el stock en la cantidad especificada
        self.stock += cantidad
        print(f"Se reabastecieron {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

if __name__ == "__main__":
    # Crear un producto con valores iniciales
    producto = Producto("Laptop", 1200, 10)

    # Realizar las operaciones especificadas
    print("¿Hay 5 unidades disponibles?", producto.verificar_disponibilidad(5))
    producto.vender(3)
    print("¿Hay 8 unidades disponibles?", producto.verificar_disponibilidad(8))
    
