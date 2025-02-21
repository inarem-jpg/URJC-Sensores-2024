#!/usr/bin/env python3

############################################################
# Práctica 6 - Sensores y Actuadores
#
# Autoras: Henar Contreras y Rebeca Castilla
#
# URJC - Robótica Software
#############################################################
import RPi.GPIO as GPIO
import signal
import time
import sys
import os

S_F = 4
S_P = 18
LED = 21

MAX = 10

# Variable donde guardar el tiempo
# que lleva sin detectar humedad
T = time.time()

GPIO.setmode(GPIO.BCM)
# Debemos configurar los pins como salida
# para que puedan ser activados o
# desactivados por código
GPIO.setup(S_P, GPIO.IN)
GPIO.setup(S_F, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def callbackSalir (senial, cuadro):
    # Ponemos este print para que ^C quede en la siguiente linea
    print (" ")
    # Deshacemos las configuraciones
    GPIO.cleanup()
    sys.exit(0)


def callbackPresence(canal):
    """
    Comprueba el estado del reedswitch, el tiempo, y, en función de este tiempo,
    el estado al que debemos poner las LEDs.
    """
    
    # Accedemos a la global
    global T

    if GPIO.input(S_F) == GPIO.LOW:
        print("Llego aquí, tiempo: ", T)
        while (time.time() - T) < MAX:
            if GPIO.input(S_P) == GPIO.HIGH:
                print("Detectó algo")
                # Enciende la LED
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(2)
            else:
                print("No hay cristianos en la costa")
        else:
            print("No activamos el sensor de presencia")
            # Enciende la LED
            GPIO.output(LED, GPIO.LOW)
    else:
        print("Idle")

def callbackPressure(canal):
    """
    Si detecta que se pulsa lo enciende, de otra manera lo apaga.
    """

    # Nos interesa acceder al valor de la global
    global T
    
    # Si detecta presión, debe empezar el temporizador
    if GPIO.input(S_F) == GPIO.LOW:
        print("Ha sido presionado tata")
        T = time.time()
    if GPIO.input(S_F) == GPIO.HIGH:
        print("Sin presión")
        
if __name__ == '__main__':
    # Añadimos el event de detectar cualquier edge (R/F) en el reedswitch
    GPIO.add_event_detect(S_F, GPIO.BOTH, 
      callback=callbackPressure, bouncetime=200)
    # Añadimos el event de detectar cualquier edge (R/F) en el sensor de humedad
    GPIO.add_event_detect(S_P, GPIO.BOTH, 
      callback=callbackPresence, bouncetime=200)
      
    # Acabar
    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()
