import pygame
from constantes import *
import math

class Bala:
    def __init__(self, x, y, objetivo_x, objetivo_y, daño):
        self.x = x
        self.y = y

        # Velocidad de la bala
        self.velocidad = BALA_VELOCIDAD
        # Tamaño de la bala
        self.ancho = BALA_ANCHO
        self.alto = BALA_ALTO
        # Color de la bala
        self.color = BALA_COLOR
        # Daño de la bala
        self.daño = daño
        
        # Calculamos la distancia hacia el objetivo con pitágoras
        dx = objetivo_x - x
        dy = objetivo_y - y
        distancia = math.sqrt(dx**2 + dy**2)

        # Normalizamos el vector para mantener la dirección
        if distancia != 0:
            self.dir_x = dx / distancia
            self.dir_y = dy / distancia
        else:
            self.dir_x = 0
            self.dir_y = 0
        
        # Dibujamos la bala
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load("assets/imagenes/bala.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        
    def actualizar(self):
        # Mover la bala en la dirección calculada con la velocidad asignada
        self.x += self.dir_x * self.velocidad
        self.y += self.dir_y * self.velocidad

        # Actualizamos la posición 
        self.rect.topleft = (self.x, self.y)
    
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
