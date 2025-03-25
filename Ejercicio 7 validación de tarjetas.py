class TarjetaDeCredito:
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    @staticmethod
    def validar_tarjeta(numero):
        # Convertir el número de tarjeta en una lista de dígitos
        digitos = [int(d) for d in str(numero)]
        
        # Doblar cada segundo dígito empezando desde la derecha
        for i in range(len(digitos) - 2, -1, -2):
            digitos[i] *= 2
            if digitos[i] > 9:
                digitos[i] = digitos[i] - 9
        
        # Sumar todos los dígitos
        suma_total = sum(digitos)
        
        # Verificar si la suma es divisible por 10
        return suma_total % 10 == 0

# Ejemplo de uso
numero_tarjeta = 4532015112830366  # Este es un número de tarjeta válido para el ejemplo
tarjeta = TarjetaDeCredito(numero_tarjeta)

if TarjetaDeCredito.validar_tarjeta(numero_tarjeta):
    print("El número de tarjeta es válido.")
else:
    print("El número de tarjeta no es válido.")