# --- Pantalla ---
ANCHO = 1280
ALTO = 720
FPS = 60
COLOR_FONDO = (0, 0, 0)

# --- Jugador ---
JUGADOR_ANCHO = 40
JUGADOR_ALTO = 40
JUGADOR_COLOR = (0, 255, 0)
JUGADOR_VELOCIDAD = 5
JUGADOR_VIDA = 200

# --- Barra de vida jugador ---
JUGADOR_BARRA_ANCHO = 40
JUGADOR_BARRA_ALTO = 6
COLOR_BARRA_JUGADOR = (0, 200, 0)
COLOR_BARRA_JUGADOR_FONDO = (60, 60, 60)

# --- Bala ---
BALA_ANCHO = 20
BALA_ALTO = 20
BALA_COLOR = (0, 150, 255)
BALA_VELOCIDAD = 8
BALA_DAÑO = 20

# --- Disparo automatico ---
COOLDOWN_DISPARO = 500  # ms

# --- Enemigos base ---
ENEMIGO_ANCHO = 60
ENEMIGO_ALTO = 60

# --- Enemigo Lento ---
ENEMIGO_LENTO_COLOR = (255, 150, 0)
ENEMIGO_LENTO_VELOCIDAD = 2
ENEMIGO_LENTO_VIDA = 60
ENEMIGO_LENTO_DAÑO = 8

# --- Enemigo Rápido ---
ENEMIGO_RAPIDO_COLOR = (255, 0, 0)
ENEMIGO_RAPIDO_VELOCIDAD = 4
ENEMIGO_RAPIDO_VIDA = 40
ENEMIGO_RAPIDO_DAÑO = 12

# --- Enemigo Tanque ---
ENEMIGO_TANQUE_COLOR = (100, 100, 255)
ENEMIGO_TANQUE_VELOCIDAD = 1
ENEMIGO_TANQUE_VIDA = 150
ENEMIGO_TANQUE_DAÑO = 20

# --- Barra de vida enemigo ---
ENEMIGO_BARRA_ANCHO = 30
ENEMIGO_BARRA_ALTO = 4
COLOR_BARRA_ENEMIGO = (200, 0, 0)
COLOR_BARRA_ENEMIGO_FONDO = (60, 0, 0)

# ------------------- NIVELES ----------------
NIVELES = {
    1: {"lento": 5, "rapido": 0, "tanque": 0},
    2: {"lento": 6, "rapido": 2, "tanque": 0},
    3: {"lento": 4, "rapido": 3, "tanque": 1},
    4: {"lento": 5, "rapido": 4, "tanque": 2},
    5: {"lento": 6, "rapido": 5, "tanque": 3},
    6: {"lento": 10, "rapido": 6, "tanque": 4},
}

# Tiempo entre niveles (ms)
TIEMPO_ENTRE_NIVELES = 3000