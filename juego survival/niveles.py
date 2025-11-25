import random
from constantes import *
from enemigo import *


def generar_posicion_por_el_borde():
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    if borde == "arriba":
        x = random.randint(0, ANCHO - ENEMIGO_ANCHO)
        y = 0

    elif borde == "abajo":
        x = random.randint(0, ANCHO - ENEMIGO_ANCHO)
        y = ALTO - ENEMIGO_ALTO

    elif borde == "izquierda":
        x = 0
        y = random.randint(0, ALTO - ENEMIGO_ALTO)

    else:  # derecha
        x = ANCHO - ENEMIGO_ANCHO
        y = random.randint(0, ALTO - ENEMIGO_ALTO)

    return x, y

def generar_enemigos_por_nivel(nivel):
    datos = NIVELES[nivel]   #  diccionario con cantidades exactas
    lista = []

    # Generar enemigos lentos
    for _ in range(datos["lento"]):
        x, y = generar_posicion_por_el_borde()
        lista.append(EnemigoLento(x, y))

    # Generar enemigos rápidos
    for _ in range(datos["rapido"]):
        x, y = generar_posicion_por_el_borde()
        lista.append(EnemigoRapido(x, y))

    # Generar enemigos tanque
    for _ in range(datos["tanque"]):
        x, y = generar_posicion_por_el_borde()
        lista.append(EnemigoTanque(x, y))

    return lista