# p3-interrupciones

## Details
Fecha: 30/10/2024.

Autoras: Castilla Puerta, Rebeca y Contreras Mateos, Henar.

Objetivo: Encendido de LEDs cuando un botón es pulsado, apagado al soltarlo.

Resumen: Contiene un primer código básico que imprime "El botón ha sido pulsado" 
cuando, efectivamente, el botón ha sido pulsado, luego, contien 3 códigos con 
funcionalidades distintas cuyo fin es hacer un programa en los que el outcome sea 
el mismo, el encendido de dos LED cuando el respectivo botón es pulsado, y el apagado
de ambos cuando los botones son soltados. 

Buscando si LEDs era un sustantivo masculino o femenino hemos descubierto que el 
plural de LED es "ledes" y me niego a usarlo, esperamos que lo entiendas.

Por motivos estéticos hemos usado dos LEDs blancos (?) en vez de uno verde y uno 
rojo (La verdad las blancas son más bonitas). La función Wait_for_Edge tiene unas 
limitaciones que impiden que un mismo LED ejecute la intrucción de encendido 2 veces 
seguidas, es necesario ir alternando los botones pulsados.
Al principio tuvimos problemas con el encendido de los LEDs ya que se nos olvidó 
completamente conectarlos a tierra :D.

No eran códigos difíciles una vez entendías bien el funcionamiento de cada función 
que se pedía (waitForEdge, AddEvent, y luego la implementación sin interrupciones)
El único problema que nos ha dado el código que no hemos conseguido solucionar, 
es en el sinInterrupcionesMejorado.py, en el cual nos ejecuta el comando 
print("boton x encendido") en bucle durante toda la pulsación, hasta que se suelta.

## Video 1: (interrupcionEdgeBueno.py) 
https://github.com/user-attachments/assets/0d17dda0-c563-447f-a882-97823d9fe067
## Video 1: (interrupcionEdgeMejorado.py)
https://github.com/user-attachments/assets/38848878-9d65-49f8-a718-b2b53f46e629
## Video 1: (interrupcionEventMejorado.py)
https://github.com/user-attachments/assets/c4a3706f-02b0-4db4-a33d-acd0dd471cfd
## Video 1: (sinInterrupcionesMejorado.py)
https://github.com/user-attachments/assets/d8490917-262d-4471-b99a-4eae350e9593

