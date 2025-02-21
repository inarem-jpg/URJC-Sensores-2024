# P5-US

## Details
Fecha: 21/11/2024.

Autoras: Castilla Puerta, Rebeca y Contreras Mateos, Henar.

Objetivo: Encendido de LEDs en función de diferentes thresholds de distancia 
cuando un sensor capta el rebote de un ultrasonido.

Resumen: Contiene un primer código básico que detecta la distancia entre la 
superficie en la que ha rebotado el ultra sonido y el sensor. Luego, en función de 
estas distancias, enciende tres LEDs: verde, amarilla o roja. 

Según la datasheet del sensor de ultrasonidos HC-SR04 el mínimo rango es 2cm y el
 máximo 4m. Para la implementación de la práctica hemos aplicado unos rangos de 
máximo un metro para más simple manejo en clase, y un rango mínimo de 3.5cm, 
puesto que a partir de esa distancia da el error de interpretar la distancia 
excesivamente cercana como distancias aleatorias incorrectas.

Los rangos pues, quedan de esta manera:
  - verde [4.5, 80]
  - amarillo (3.5, 4.5)
  - rojo (x < 3.5) ∪ (80 > x)

## Video
https://github.com/user-attachments/assets/7dba4b1d-c420-44a4-a49d-82a972c83fb6
