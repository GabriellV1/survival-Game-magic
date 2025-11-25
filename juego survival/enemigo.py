import pygame 
from constantes import *
import math

class Enemigo:
    def __init__(self, x, y):
         #posicion:
        self.x = x 
        self.y = y
        #tamaño genral del enemigo
        self.ancho = ENEMIGO_ANCHO
        self.alto = ENEMIGO_ALTO

        #verificar si esta vivo
        self.vivo = True
        #dibujar al enemigo
        self.rect = pygame.Rect(self.x, self. y, self.ancho, self.alto)

    def mover(self, enemigo_x, enemigo_y):
        if not self.vivo:
            return
        #calculamos la distancia hacia el objetivo
        dx = enemigo_x - self.x 
        dy = enemigo_y - self.y 
        distancia=math.sqrt(dx**2 + dy**2) 

        #Normalizamos pára mantener la direccion
        if distancia != 0:
             dx /= distancia
             dy /= distancia
        self.x += dx * self.velocidad
        self.y += dy * self.velocidad

        #actualizamos la posicion 
        self.rect.topleft = (self.x, self.y)
    
    def recibir_daño(self, cantidad):
        if self.vivo:
            self.vida-= cantidad
            if self.vida <= 0:
                self.vida = 0
                self.vivo = False
    
    def atacar(self, jugador):
        if self.vivo and self.rect.colliderect(jugador.rect):
            jugador.recibir_daño(self.daño)


    def dibujar_barra_vida(self, pantalla):
        # Posición de la barra (arriba del enemigo)
        barra_x = self.x + (self.ancho // 2) - (ENEMIGO_BARRA_ANCHO // 2)
        barra_y = self.y - 8  # un poquito arriba
          # Fondo gris
        pygame.draw.rect(pantalla, COLOR_BARRA_ENEMIGO_FONDO,(barra_x, barra_y, ENEMIGO_BARRA_ANCHO, ENEMIGO_BARRA_ALTO))
        # Proporción de vida
        vida_relativa = self.vida / self.vida_max
        ancho_vida = ENEMIGO_BARRA_ANCHO * vida_relativa
        # Barra verde (vida)
        pygame.draw.rect(pantalla, COLOR_BARRA_ENEMIGO,(barra_x, barra_y, ancho_vida, ENEMIGO_BARRA_ALTO))

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
        self.dibujar_barra_vida(pantalla)


class EnemigoLento(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ancho = ENEMIGO_ANCHO
        self.alto = ENEMIGO_ALTO
        self.color = ENEMIGO_LENTO_COLOR
        self.velocidad = ENEMIGO_LENTO_VELOCIDAD
        self.vida = ENEMIGO_LENTO_VIDA
        self.vida_max = ENEMIGO_LENTO_VIDA
        self.daño = ENEMIGO_LENTO_DAÑO

        #cargar imagen:
        self.imagen = pygame.image.load("assets/imagenes/enemigo_01.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))


class EnemigoRapido(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ancho = ENEMIGO_ANCHO
        self.alto = ENEMIGO_ALTO
        self.color = ENEMIGO_RAPIDO_COLOR
        self.velocidad = ENEMIGO_RAPIDO_VELOCIDAD
        self.vida = ENEMIGO_RAPIDO_VIDA
        self.vida_max = ENEMIGO_RAPIDO_VIDA
        self.daño = ENEMIGO_RAPIDO_DAÑO

        #cargar imagen:
        self.imagen = pygame.image.load("assets/imagenes/enemigo_02.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))


class EnemigoTanque(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ancho = ENEMIGO_ANCHO
        self.alto = ENEMIGO_ALTO
        self.color = ENEMIGO_TANQUE_COLOR
        self.velocidad = ENEMIGO_TANQUE_VELOCIDAD
        self.vida = ENEMIGO_TANQUE_VIDA
        self.vida_max = ENEMIGO_TANQUE_VIDA
        self.daño = ENEMIGO_TANQUE_DAÑO

       #cargar imagen:
        self.imagen = pygame.image.load("assets/imagenes/enemigo_03.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
