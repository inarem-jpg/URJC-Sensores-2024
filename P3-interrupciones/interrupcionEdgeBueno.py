#!/usr/bin/env python3

import signal
import sys
import time
import RPi.GPIO as GPIO

PULSADOR_1 = 16

def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    # Ponemos este print para que ^C quede en la siguiente linea
    print (" ")
    # Deshacemos las configuraciones
    GPIO.cleanup ()
    sys.exit(0)

def callbackBotonPulsado():
    print("El boton se ha pulsado")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PULSADOR_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    # Reconoce el CNTRL C para salir
    signal.signal(signal.SIGINT, callbackSalir)
    while True:
        # Añadimos bounce time para que capte los pulsos que le damos
        # y no ninguna extra.
        GPIO.wait_for_edge(PULSADOR_1, GPIO.RISING, bouncetime=200)
        callbackBotonPulsado()
