import pygame
import math
from constantes import *
from bala import Bala
class Jugador:
    def __init__(self, x, y):
        #posicion:
        self.x = x 
        self.y = y
        self.daño = BALA_DAÑO
        #Velociadad de movimiento
        self.velocidad = JUGADOR_VELOCIDAD
        #tamaño del jugador
        self.ancho = JUGADOR_ANCHO
        self.alto= JUGADOR_ALTO
        #vida del jugador
        self.vida = JUGADOR_VIDA
        #color del jugador
        self.color = JUGADOR_COLOR
        #verificar si esta vivo
        self.vivo = True
        #dibujar al jugador
        self.rect = pygame.Rect(self.x, self. y, self.ancho, self.alto)
        self.imagen = pygame.image.load("assets/imagenes/jugador.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        #disparo automactivo
        self.cooldown = COOLDOWN_DISPARO
        #Disparo automatico
        self.tiempo_ultimo_disparo = 0
    
    def mover(self):
        if not self.vivo:
            return

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.y -= self.velocidad

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.y += self.velocidad

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.velocidad

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
        
        #actualizamos la posicion 
        self.rect.topleft = (self.x, self.y)
    
    def limitar_pantalla(self, ancho, alto):
        #No permitir que el jugador salga de arriba o abajo de la pantalla:
                                                                    
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0 

        #No permitir que el jugador salga de izquierda o derecha de la pantalla:

        if self.x + self.ancho > ancho:
            self.x = ancho - self.ancho

        if self.y + self.alto > alto:
            self.y = alto - self.alto
        
        #actualizamos la posicion 
        self.rect.topleft = (self.x, self.y)

    def recibir_daño(self, cantidad):
        if self.vivo:
            self.vida-= cantidad
            if self.vida <=0:
                self.vida = 0
                self.vivo = False
    
    def disparo_automatico(self, enemigos, balas):

        #verifica si el jhugador sigue vivo
        if not self.vivo:
            return
        # obtiene el tiempo actual en milisegundos
        tiempo_actual = pygame.time.get_ticks()  
        objetivo = None
        # Buscar el enemigo más cercano
        if tiempo_actual - self.tiempo_ultimo_disparo >= self.cooldown:  
            # empezamos con infinito para comparar distancias
            distancia_min = float('inf') 

            for enemigo in enemigos:
                if enemigo.vivo:
                    dx = enemigo.x - self.x
                    dy = enemigo.y - self.y
                    distancia = math.sqrt(dx**2 + dy**2) 

                    if distancia < distancia_min:
                        distancia_min = distancia
                        objetivo = enemigo

        # Si encontramos un objetivo, disparamos
        if objetivo:
            nueva_bala = Bala( self.x + self.ancho//2, self.y + self.alto//2, objetivo.x + objetivo.ancho//2,objetivo.y + objetivo.alto//2, self.daño)
            # agregamos la bala a la lista de balas del juego
            balas.append(nueva_bala)  
            # reiniciamos el cooldown
            self.tiempo_ultimo_disparo = tiempo_actual
    
    def dibujar_barra_vida(self, pantalla):
        # Posición de la barra (arriba del jugador)
        barra_x = self.x + (self.ancho // 2) - ( JUGADOR_BARRA_ANCHO// 2)
        barra_y = self.y - 10   # un poco arriba del jugador

        # Fondo gris
        pygame.draw.rect(pantalla,COLOR_BARRA_JUGADOR_FONDO,(barra_x, barra_y, JUGADOR_BARRA_ANCHO, JUGADOR_BARRA_ALTO))

        # Proporción de vida
        vida_relativa = self.vida / JUGADOR_VIDA
        ancho_vida = JUGADOR_BARRA_ANCHO * vida_relativa

        # Barra verde (vida)
        pygame.draw.rect(pantalla,COLOR_BARRA_JUGADOR,(barra_x, barra_y, ancho_vida, JUGADOR_BARRA_ALTO))

    
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
        self.dibujar_barra_vida(pantalla)

     


    
      
            


