import pygame

def colision_bala_enemigo(balas, enemigos):
#Detecta si alguna bala tocó a algún enemigo La bala desaparece y el enemigo recibe daño.
    for bala in balas[:]:  # copiar lista para evitar errores al eliminar
        for enemigo in enemigos[:]:
            if enemigo.vivo and bala.rect.colliderect(enemigo.rect):
                enemigo.recibir_daño(bala.daño)
                
                if bala in balas:
                    balas.remove(bala)

                if not enemigo.vivo:
                    enemigos.remove(enemigo)
                    
                    break  # la bala ya desapareció → pasar a la siguiente


def colision_enemigo_jugador(jugador, enemigos):
    """
    Detecta si un enemigo tocó al jugador.
    """
    if not jugador.vivo:
        return

    for enemigo in enemigos:
        if enemigo.vivo and enemigo.rect.colliderect(jugador.rect):
            jugador.recibir_daño(enemigo.daño)
            break  # solo un golpe por frame