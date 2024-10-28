# Microbit-Siguelineas
Algoritmos para siguelineas con el robot Maqueen Plus, contamos también con programas para el control de microbit a Radio Control.
Módulo utilizado para el control del Maqueen pro: "lib_robot_maqueen.py"
## Python-ide: https://python.microbit.org/
En esta carpeta se encuentran todos los programas en python que hemos programado usando este entorno de desarrollo online(IDE). Para añadir el módulo del maqueen-pro podemos pulsar en project => Open... y seleccionar el archivo lib_robot_maqueen.py de nuestro ordenador. También podemos arrastrar el archivo al IDE directamente.
Este entorno no tiene versión de aplicación: https://tech.microbit.org/software/python-editor/ mientras que makecode sí que tiene: https://support.microbit.org/support/solutions/articles/19000013750-using-the-micro-bit-editors-offline

  - Los archivos .py los podemos editar en la IDE y descargarlos como .hex
  - Los archivos .hex los podemos subir directamente a la placa microbit arrastrando el archivo en windows

### Tests:
Los programas que utilizan la libreria de maqueen-pro son propensos a dar errores: "line 4 memory error". Reiniciar la placa puede hacer que el error desaparezca o hacer cambios en
el programa.

# Control remoto
Para poder medir como de bueno es el algoritmo siguelineas comparamos cual es el tiempo que puede hacer el robot controlado por un humano. En principio tenemos el objetivo de hacerlo con una extension específica para microbit con app-inventor.
