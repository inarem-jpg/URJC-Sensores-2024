#!/usr/bin/env python3

############################################################
# Práctica 3 - Sensores y Actuadores
#
# Autoras: Henar Contreras y Rebeca Castilla
#
# URJC - Robótica Software
#
# Por motivos estéticos usamos dos LEDs de luz azul. 
# Como aclaración de cara a los videos de la funcionalidad
# comentamos para cada led a cuál corresponde
#############################################################

import RPi.GPIO as GPIO
import signal
import time
import sys

PULSADOR_GREEN = 16
PULSADOR_RED = 12

# Led izquierdo 
LED_GREEN = 25
# Led derecha 
LED_RED = 22

def callbackSalir (senial, cuadro):
    # Ponemos este print para que ^C quede en la siguiente linea
    print (" ")
    # Deshacemos las configuraciones
    GPIO.cleanup()
    sys.exit(0)

def callback1Pulsado(canal):
    """
    Si detecta que se pulsa lo enciende, de otra manera lo apaga.
    """
    
    if GPIO.input(PULSADOR_GREEN) == GPIO.LOW:
        print("El boton del led green se ha pulsado (led IZQ)")
        GPIO.output(LED_GREEN, GPIO.HIGH)
    else:
        GPIO.output(LED_GREEN, GPIO.LOW)
    
def callback2Pulsado(canal):
    """
    Si detecta que se pulsa lo enciende, de otra manera lo apaga.
    """
    
    if GPIO.input(PULSADOR_RED) == GPIO.LOW:
        print("El boton del led rojo se ha pulsado (led RJ)")
        GPIO.output(LED_RED, GPIO.HIGH)
    else:
        GPIO.output(LED_RED, GPIO.LOW)


if __name__ == '__main__':
    # Especificamos cómo vamos a tratar los puertos
    GPIO.setmode(GPIO.BCM)
    # Configuramos los pulsadores en pull up
    GPIO.setup(PULSADOR_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PULSADOR_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Configuramos los puertos de los LEDs para poder encenderlos con código
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)
    
    # Añadimos el event de detectar cualquier edge (R/F) en el botón del led verde
    GPIO.add_event_detect(PULSADOR_GREEN, GPIO.BOTH, 
      callback=callback1Pulsado, bouncetime=200)
    # Añadimos el event de detectar cualquier edge (R/F) en el botón del led verde
    GPIO.add_event_detect(PULSADOR_RED, GPIO.BOTH, 
      callback=callback2Pulsado, bouncetime=200)
    
    # Acabar
    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()

