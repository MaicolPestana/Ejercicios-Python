class CuentaBancaria:
    def __init__(self, titular, saldo):
        # Inicializa los atributos de la cuenta bancaria.
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        # Agrega dinero a la cuenta bancaria.
        self.__saldo += monto

    def consultar_saldo(self):
        # Devuelve el saldo actual de la cuenta.
        return self.__saldo

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes_anual):
        # Inicializa los atributos de CuentaBancaria y el porcentaje de interés anual.
        CuentaBancaria.__init__(self, titular, saldo)
        self.__interes_anual = interes_anual

    def aplicar_interes(self):
        # Aplica el interés anual al saldo actual.
        self.depositar(self.consultar_saldo() * (self.__interes_anual / 100))

    def consultar_interes(self):
        # Devuelve el porcentaje de interés anual.
        return self.__interes_anual

if __name__ == "__main__":
    # Crea una cuenta de ahorro y muestra detalles.
    cuenta = CuentaAhorro("Juan Perez", 1000, 5)
    print("Saldo inicial:", cuenta.consultar_saldo())
    print("Interés anual:", cuenta.consultar_interes(), "%")

    # Aplica el interés y muestra el saldo actualizado.
    cuenta.aplicar_interes()
    print("Saldo después de aplicar interés:", cuenta.consultar_saldo())
