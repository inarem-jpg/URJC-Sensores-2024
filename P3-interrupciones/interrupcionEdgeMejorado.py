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

def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    # Ponemos este print para que ^C quede en la siguiente linea
    print (" ")
    # Deshacemos las configuraciones
    GPIO.cleanup ()
    sys.exit(0)

def callback1Pulsado():
    print("El boton 1 se ha pulsado (led verde)")
    GPIO.output(LED_GREEN, GPIO.HIGH)
def callback2Pulsado():
    print("El boton 2 se ha pulsado (led rojo)")
    GPIO.output(LED_RED, GPIO.HIGH)

if __name__ == '__main__':
    # Especificamos cómo vamos a tratar los puertos
    GPIO.setmode(GPIO.BCM)
    # Configuramos los pulsadores en pull up
    GPIO.setup(PULSADOR_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PULSADOR_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Configuramos los puertos de los LEDs para poder encenderlos con código
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(LED_RED, GPIO.OUT)
    
    # Reconoce el CNTRL+C para salir
    signal.signal(signal.SIGINT, callbackSalir)
    while True:
        # Si capta el edge
        if (GPIO.wait_for_edge(PULSADOR_GREEN, GPIO.FALLING, bouncetime=200) != None):
            # Enciende el led verde
            callback1Pulsado()
        # Si capta el edge
        if (GPIO.wait_for_edge(PULSADOR_GREEN, GPIO.RISING, bouncetime=200) != None):
            # Apaga el led verde
            GPIO.output(LED_GREEN, GPIO.LOW)
        # Si capta el edge
        if (GPIO.wait_for_edge(PULSADOR_RED, GPIO.FALLING, bouncetime=200) != None):
            # Enciende el led rojo
            callback2Pulsado()
        # Si capta el edge
        if (GPIO.wait_for_edge(PULSADOR_RED, GPIO.RISING, bouncetime=200) != None):
            # Apaga el led rojo
            GPIO.output(LED_RED, GPIO.LOW)
            
            
            
