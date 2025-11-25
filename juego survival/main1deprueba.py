import pygame
import random
from constantes import *
from player import Jugador
from bala import Bala
from enemigo import Enemigo

pygame.init()

# Ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Prueba Disparo Automático")

# Reloj
reloj = pygame.time.Clock()

# Crear jugador
jugador = Jugador(ANCHO // 2, ALTO // 2)

# Lista de enemigos
enemigos = []
for _ in range(5):
    x = random.randint(0, ANCHO - ENEMIGO_ANCHO)
    y = random.randint(0, ALTO - ENEMIGO_ALTO)
    enemigo = Enemigo(x, y)
    # Asignamos atributos básicos para que se muevan
    enemigo.velocidad = 1
    enemigo.vida = 50
    enemigo.daño = 10
    enemigos.append(enemigo)

# Lista de balas
balas = []

# Bucle principal
ejecutar = True
while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False

    # Actualizar jugador
    jugador.mover()
    jugador.limitar_pantalla(ANCHO, ALTO)

    # Disparo automático
    jugador.disparo_automatico(enemigos, balas)

    # Mover balas
    for bala in balas[:]:
        bala.actualizar()
        # Quitar bala si sale de pantalla
        if (bala.x < 0 or bala.x > ANCHO or
            bala.y < 0 or bala.y > ALTO):
            balas.remove(bala)

    # Mover enemigos hacia jugador
    for enemigo in enemigos:
        enemigo.mover(jugador.x, jugador.y)

    # Colisión simple: bala con enemigo
    for bala in balas[:]:
        for enemigo in enemigos[:]:
            if enemigo.rect.colliderect(bala.rect):
                enemigo.vida -= BALA_DAÑO
                if enemigo.vida <= 0:
                    enemigos.remove(enemigo)
                if bala in balas:
                    balas.remove(bala)
                break

    # Dibujar todo
    pantalla.fill((0, 0, 0))
    jugador.dibujar(pantalla)
    for bala in balas:
        bala.dibujar(pantalla)
    for enemigo in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), enemigo.rect)

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()