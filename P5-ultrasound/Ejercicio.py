#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Pines del sensor
PIN_TRIGGER = 17
PIN_ECHO = 27

# Pines de los leds
LED_V = 22
LED_R = 24
LED_A = 23
      
def encender(led):
      """
      Activa el led en el pin especificado.
      """
      
      GPIO.output(led,GPIO.HIGH)
      
def apagar(led):
      """
      Desactiva el led en el pin especificado.
      """
      
      GPIO.output(led,GPIO.LOW)

def ledCode(led):
      """
      Enciende el led en el pin especificado durante 1 segundo
      y después lo apaga.
      """
      
      encender(led)
      time.sleep(2)
      apagar(led)

try:
      GPIO.setmode(GPIO.BCM)

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)
      
      GPIO.setup(LED_V,GPIO.OUT)
      GPIO.setup(LED_A,GPIO.OUT)
      GPIO.setup(LED_R,GPIO.OUT)
      
      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      
      while True:
            salida = input("'Y' para salir\n")
            if salida == "Y":
                  break
            else:
                  print ("Esperando a que se estabilice el US")
                  time.sleep(2)

                  GPIO.output(PIN_TRIGGER, GPIO.HIGH)
                  time.sleep(0.00001)
                  GPIO.output(PIN_TRIGGER, GPIO.LOW)

                  while GPIO.input(PIN_ECHO)==0:
                        inicioPulso = time.time()
                  while GPIO.input(PIN_ECHO)==1:
                        finPulso = time.time()

                  duracionPulso = finPulso - inicioPulso
                  distancia = round(duracionPulso * 17150, 2)
                  print ("Distancia: ", distancia, " cm")
                  
                  # Distancia de posibles fallos
                  if distancia < 3.5 or distancia > 80:
                        ledCode(LED_R)
                  # Distancia prudencial
                  elif distancia < 4.5 and distancia > 3.5:
                        ledCode(LED_A)
                  # Distancia correcta para nuestro threshold
                  else:
                        ledCode(LED_V)

finally:
      GPIO.cleanup()
