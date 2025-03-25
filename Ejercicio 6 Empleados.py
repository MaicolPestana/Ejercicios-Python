class Empleado:
    # Atributo de clase para contar el número total de empleados.
    contador_empleados = 0

    def __init__(self, nombre, salario):
        # Inicializa el nombre y salario del empleado.
        self.nombre = nombre
        self.salario = salario

        # Incrementa el contador de empleados al crear uno nuevo.
        Empleado.contador_empleados += 1

    @classmethod
    def cantidad_empleados(cls):
        # Método de clase para devolver el número total de empleados.
        return cls.contador_empleados

if __name__ == "__main__":
    # Crear empleados y mostrar el número total.
    emp1 = Empleado("Carlos", 3000)
    emp2 = Empleado("Ana", 3500)

    print("Total de empleados:", Empleado.cantidad_empleados())

    
