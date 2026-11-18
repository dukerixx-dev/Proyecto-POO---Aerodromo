from Metodo_Pago import Metodo_Pago
from Gerente import Gerente
from Cliente import Cliente
from Personal import Personal
from Avion import Avion
from datetime import date
if __name__ == "__main__":
    #ejemplo de metodo de pago
    debito = Metodo_Pago(None, 67, None, None, None, None, 1234)
    credito = Metodo_Pago("xd", 67, 123, 676767, date(2067,11,22), 676, 1167)