from datetime import date
class Metodo_Pago:
    def __init__(self, tipo, nombre_full, rut, num_tarjeta, fecha_vencimiento, cvv, clave):
        self.tipo = tipo
        self.nombre_full = nombre_full
        self.rut = rut
        self.num_tarjeta = num_tarjeta
        self.fecha_vencimiento = fecha_vencimiento
        self.cvv = cvv
        self.clave = clave
    