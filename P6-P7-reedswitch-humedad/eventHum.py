#!/usr/bin/env python3

############################################################
# Práctica 6 - Sensores y Actuadores
#
# Autoras: Henar Contreras y Rebeca Castilla
#
# URJC - Robótica Software
#
# 
# 
#############################################################
import RPi.GPIO as GPIO
import signal
import sys

SENSOR = 23
LED = 26

GPIO.setmode(GPIO.BCM)
# Debemos configurar los pins como salida
# para que puedan ser activados o
# desactivados por código.
GPIO.setup(SENSOR, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

def callbackSalir (senial, cuadro):
    # Ponemos este print para que ^C quede en la siguiente linea
    print (" ")
    # Deshacemos las configuraciones
    GPIO.cleanup()
    sys.exit(0)

def callbackHum(canal):
    """
    Si detecta que se pulsa lo enciende, de otra manera lo apaga.
    """
    
    if GPIO.input(SENSOR) == GPIO.LOW:
        print("humedad")
        GPIO.output(LED, GPIO.HIGH)
    else:
        print("no humedad")
        GPIO.output(LED, GPIO.LOW)
        
if __name__ == '__main__':
    # Configuramos los pulsadores en pull up
    GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Añadimos el event de detectar cualquier edge (R/F) en el botón del led verde
    GPIO.add_event_detect(SENSOR, GPIO.BOTH, 
      callback=callbackHum, bouncetime=200)
      
    # Acabar
    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()
