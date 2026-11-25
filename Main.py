#time guarda una hora y un minuto especifico, time(8, 0) son las 8:00 am
#timedelta representa un dia, lo sumamos para poder pasar a siguiente fecha
from datetime import date, time, timedelta

# Importamos las clases a usar en main
from Destino import Destino
from Avion import Avion 
from Vuelo import Vuelo
from Registro import Registro
from Metodo_Pago import Metodo_Pago

# De vista.py traemos las funciones para pedir un destino
# mostrar los vuelos encontrados y mostrar los medios de pago disponibles
from Vista import pedir_destino, mostrar_vuelos, mostrar_medios_pago

def cargar_vuelos(registro):
    # Cree los aviones con sus respectivos atributos

    cessna_310 = Avion("AV01", "Cessna 310", 5, 910)
    caravan = Avion("AV02", "Cessna 208 Caravan", 9, 1315)
    let_410 = Avion("AV03", "LET 410 UVP-E20", 19, 1800)

    # Guarde cada destino con sus respectivos nombre, precio del pasaje y precio por kilo

    cochamo = Destino("Cochamo", 20000, 5000)
    puelo_bajo = Destino("Puelo Bajo", 20000, 5000)
    contao = Destino("Contao", 20000, 5000)
    rio_negro = Destino("Rio Negro", 25000, 6000)
    pupelde = Destino("Pupelde", 25000, 6000)
    chepu = Destino("Chepu", 30000, 8000)
    ayacara = Destino("Ayacara", 30000, 8000)
    pillan = Destino("Pillan", 40000, 12000)
    renihue = Destino("Renihue", 40000, 12000)
    isla_quenac = Destino("Isla Quenac", 40000, 12000)
    palqui = Destino("Palqui", 40000, 12000)
    chaiten = Destino("Chaiten", 50000, 15000)
    santa_barbara = Destino("Santa Barbara", 50000, 15000)    


# Usamos una lista de tuplas para almacenar las salidas que se repiten cada dia
# En cada fila se agruparon 3 datos en orden, el destino, avion y la hora de salida
    salidas = [
        (cochamo, cessna_310, time(8, 0)),
        (puelo_bajo, caravan, time(8, 0)),
        (contao, let_410, time(8, 0)),
        (rio_negro, cessna_310, time(10, 30)),
        (pupelde, caravan, time(10, 30)),
        (chepu, let_410, time(10, 30)),
        (ayacara, cessna_310, time(13, 0)),
        (pillan, caravan, time(13, 0)),
        (renihue, let_410, time(13, 0)),
        (isla_quenac, cessna_310, time(15, 30)),
        (palqui, caravan, time(15, 30)),
        (chaiten, let_410, time(15, 30)),
        (santa_barbara, cessna_310, time(18, 0)),
    ]

    numero = 1
    fecha = date(2026, 11, 25)

    # Mediante un ciclo for damos 1 vuelta por cada dia como ejemplo
    # Con esto leemos las 13 filas para esta fecha
    # En la primera vuelta destino, avion y hora toman los valores de la primera tupla
    for dia in range(7):
        for destino, avion, hora in salidas: 
            # Con str convertimos el numero en texto para poder formar V1, V2, V3 y asi es meramente estetico 
            # y en parte igual facil de entender visualmente 
            codigo = "V" + str(numero)  
            vuelo = Vuelo(codigo, destino, avion, fecha, hora, "programado")
            registro.agregar_vuelo(vuelo) # Guardamos el vuelo que acabamos de crear en el registro
            numero = numero + 1 # Asi mismo aumentamos el numero para ir aumentando el codigo del vuelo tipo V2, V3, etc

        fecha = fecha + timedelta(days=1) # Sumamos un dia a la fecha para la siguiente vuelta del ciclo for


if __name__ == "__main__":
    registro = Registro()
    # Esto se encarga de agregar los vuelos al registro para despues poder buscarlos y mostrarlos en la vista
    cargar_vuelos(registro)
    # Con esto el Main se encarga de consultar para poder devolverle los vuelos que tiene que mostrar
    
    medios_pago = [Metodo_Pago("Debito"), Metodo_Pago("Credito")]
    mostrar_medios_pago(medios_pago)
    destino_buscado = pedir_destino()
    vuelos_encontrados = registro.buscar_por_destino(destino_buscado)
    mostrar_vuelos(vuelos_encontrados)


