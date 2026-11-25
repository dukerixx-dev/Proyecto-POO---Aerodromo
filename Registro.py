class Registro:
    def __init__(self):
        self.vuelos = []
        self.ventas = []
# Deje cada registro con su propia lista vacia

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def buscar_por_destino(self, nombre):
        # El .strip() fue una forma de eliminar espacios/tabulaciones 
        # El .lower() fue una forma de hacer que automaticamente transforme a minusculas todo
        # De tal manera que no importa como el usuario escriba el nombre del destino
        nombre_buscado = nombre.strip().lower()

        encontrados = []
        for vuelo in self.vuelos:
            if vuelo.destino.nombre.lower() == nombre_buscado:
                encontrados.append(vuelo)
        return encontrados
        # Con esto hacemos un recorrido por todos los vuelos para poder guardar las coincidencias en otra lista
        # Y luego retornamos esa lista con los vuelos encontrados aun asi quede vacia