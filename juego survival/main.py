import pygame
import random
from constantes import *
from player import Jugador
from bala import Bala
from enemigo import *
from colisiones import *
from niveles import *


pygame.init()

#L ventana del juego
pantalla=pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("survival")
fondo = pygame.image.load("assets/imagenes/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
#fps
reloj = pygame.time.Clock()

#creamos al jugador
jugador = Jugador(ANCHO//2, ALTO//2 )

#lista de balas y enemigos
balas=[]
enemigos=[]

#sistema de nieveles:
nivel_actual = 1
nivel_maximo = len(NIVELES)
mostrar_mensaje_nivel = True
timepo_de_mensaje = 0


# Crear enemigos de prueba
enemigos = generar_enemigos_por_nivel(nivel_actual)

#Bucle princiapl
ejecutar = True

while ejecutar:
    #eventos 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False

    
    #Actualizar al jugador
    jugador.mover()
    jugador.limitar_pantalla(ANCHO, ALTO)
    jugador.disparo_automatico(enemigos, balas)

    #Actualizar balas:
    for bala in balas:
        bala.actualizar()
    
    #Actualizar enemigo:
    for enemigo in enemigos:
        enemigo.mover(jugador.x, jugador.y)

    #colisiones:
    colision_bala_enemigo(balas, enemigos)
    colision_enemigo_jugador(jugador, enemigos)

    #Sistema de pasar de nivel:
    if len(enemigos) == 0 and jugador.vivo:
        # si acabó el nivel, mostramos mensaje 2 segundos
        if nivel_actual < nivel_maximo:
            nivel_actual += 1
            # RECOMPENSAS POR NIVEL
            jugador.vida += 5
            jugador.daño +=5
            if jugador.vida > JUGADOR_VIDA:
                 jugador.vida = JUGADOR_VIDA
                 jugador.velocidad += 1
                 if jugador.cooldown > 150: 
                     jugador.cooldown -= 10
                    
            enemigos = generar_enemigos_por_nivel(nivel_actual)
            mostrar_mensaje_nivel = True
            timepo_de_mensaje = pygame.time.get_ticks()
        else:
            # GANASTE TODOS LOS NIVELES
            pantalla.fill((0,0,0))
            texto = pygame.font.SysFont(None, 60).render("¡GANASTE EL JUEGO!", True, (255,255,255))
            pantalla.blit(texto, (ANCHO//2 - 180, ALTO//2 - 20))
            pygame.display.flip()
            pygame.time.delay(3000)
            break


    #GAME OVER:
    if not jugador.vivo:
        pantalla.fill((0,0,0))
        texto = pygame.font.SysFont(None, 60).render("GAME OVER", True, (255,0,0))
        pantalla.blit(texto, (ANCHO//2 - 120, ALTO//2 - 20))
        pygame.display.flip()
        pygame.time.delay(2000)
        break

    #dibujamos Fodo en la pnatalla
    pantalla.blit(fondo,(0,0))

    #dibujamos al jugador:
    jugador.dibujar(pantalla)

    #dibujamos el mensaje:
    if mostrar_mensaje_nivel:
        texto = pygame.font.SysFont(None, 50).render(f"Nivel {nivel_actual}", True, (255,255,255))
        pantalla.blit(texto, (ANCHO//2 - 80, 40))

        if pygame.time.get_ticks() - timepo_de_mensaje > 1500:
            mostrar_mensaje_nivel = False

    #dibujamos balas
    for bala in balas:
        bala.dibujar(pantalla)

    #dibujamos ENEMIGOS
    for enemigo in enemigos:
        enemigo.dibujar(pantalla)


    #iniciar pantalla
    pygame.display.flip()
    #fps asignados
    reloj.tick(FPS)

#salir del juego
pygame.quit()