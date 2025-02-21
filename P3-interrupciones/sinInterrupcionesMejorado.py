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

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    # Activamos resistencia pull_up_down en modo HIGH, esto es:
    # - HIGH: estado por defecto del GPIO (no se ha pulsado).
    # - LOW: estado del GPIO cuando se ha pulsado el boton.
    GPIO.setup(PULSADOR_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PULSADOR_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Configuramos los puertos de los LEDs para poder encenderlos con código
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)

    pulsado = False
    while True:
        if not GPIO.input(PULSADOR_GREEN): # la lectura siempre da 1 (HIGH/True) excepto al pulsar,
                                         # y solo en ese instante, que da 0 (LOW/False)
            if not pulsado: # con esta variable evitamos considerar más de una vez una pulsación;
                            # puede que se lea +1 vez el estado del pin antes de cambiar su estado
                            # Este fenómeno se conoce como rebote (o bounce). Algunas funciones
                            # permiten establecer un parámetro denominado "bouncetime"
                print("Botón de led verde pulsado")
                GPIO.output(LED_GREEN, GPIO.HIGH)
        else:
            # Si no esta pulsado, apaga
            GPIO.output(LED_GREEN, GPIO.LOW)
            
        if not GPIO.input(PULSADOR_RED):
            if not pulsado:
                print("Botón de led rojo pulsado")
                GPIO.output(LED_RED, GPIO.HIGH)
        else:
            # Si no esta pulsado, apaga
            GPIO.output(LED_RED, GPIO.LOW)

        time.sleep(0.5)
    
    GPIO.cleanup()
