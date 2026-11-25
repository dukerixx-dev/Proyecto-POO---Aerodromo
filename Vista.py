def pedir_destino():
    return input("Ingrese el Destino: ")

def mostrar_vuelos(vuelos):
    if len(vuelos) == 0:
        print("Sin vuelos para ese destino")
    # con el len tenemos el conteo de cuantos resultados recibio la vista

    for vuelo in vuelos:
        print()
        print("Vuelo" , vuelo.codigo)
        print("Destino:" , vuelo.destino.nombre)
        print("Fecha:", vuelo.fecha)
        print("Hora:", vuelo.hora)
        print("Avión:", vuelo.avion.modelo) 
        print("Capacidad:", vuelo.avion.capacidad_pasajeros, "pasajeros")
        print("Pasaje:", vuelo.destino.precio_pasaje, "pesos")


def mostrar_medios_pago(medios_pago):
    print("Medios de pago disponibles:")
    for medio in medios_pago:
        print(medio.tipo)

