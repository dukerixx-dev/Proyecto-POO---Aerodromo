class Vuelo:
    def __init__(self, codigo, destino, avion, fecha, hora, estado):
        self.codigo = codigo
        self.destino = destino
        self.avion = avion
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.reservas = []
        self.encomiendas = []