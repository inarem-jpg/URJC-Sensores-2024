##########################################
# Código programado por Henar Contreras
# y Rebeca Castilla.
#
# URJC Ingeniería de Robótica Software
#
# Sensores y Actuadores - Práctica 1
##########################################

# El import necesario para usar el modulo GPIO
import RPi.GPIO as GPIO

# Indicamos que vamos a usar numeración
# de pin físico (GROUND)
GPIO.setmode(GPIO.BOARD)

# Queremos usar el pin 11 como salida
GPIO.setup(11, GPIO.OUT)

# Definimos los pulsos a intensidad 100
# F.máx = 100Hz
# T = 10ms
# Pin: 11
pwm = GPIO.PWM(11, 100)

input("Pins establecidos, ahora definimos el periodo")

# Establecemos el ciclo de trabajo:
# porcentaje del periodo en el que
# la señal está en alto
pwm.start(50)

input("Se ha encendindo a intesidad 50%")
input("Ahora cambiamos el duty cycle a 1")
pwm.ChangeDutyCycle(1)

input("Lo volvemos a cambiar, esta vez a 100%")
pwm.ChangeDutyCycle(100)

# Cambiamos la frecuencia
pwm.ChangeFrequency(1000)

input("Ejecutando hasta que se pulse una tecla")

# Desactivamos el PWM
pwm.stop()
#Eliminamos nuestra confg de puertos
GPIO.cleanup()
