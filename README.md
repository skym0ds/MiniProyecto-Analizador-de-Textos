# MiniProyecto-Analizador-de-Textos
Este proyecto es una aplicación en Python con interfaz gráfica que permite analizar textos académicos, literarios o generales.
El analizador muestra:

Número de palabras.
Frecuencia de términos clave.
Sinónimos de los términos clave.
Entidades nombradas (personas, lugares, organizaciones).

Además, permite escribir directamente un texto o importar un archivo .txt para ser analizado.

## Requisitos
Tener instalado [Python] en su versión 3.13.17 
Tener instalado [Visual Studio Code]
Pip (este ya debería venir incluido en la instalación de Python)

## Instalación
Para empezar a usar este documento, necesitarás clonar el repositorio a tu sistema de archivos. Todas las instrucciones están escritas para usuarios de Windows solamente.

Entra a la carpeta en la que quieras tener el proyecto usando el Explorador de Archivos; por ejemplo en tu carpeta de `Documentos\Proyectos` o algo por el estilo.

Haz clic derecho sobre algún espacio en blanco dentro del Explorador y selecciona la opción `Abrir en Terminal`. Si no aparece, puede ser que diga `Abrir en Símbolo del Sistema`, `Abrir en PowerShell` `Abrir en CMD` o algo así. Si no aparece ninguna de estas opciones, prueba manteniendo la tecla `Shift` pulsada en tu teclado mientras haces clic derecho.

Una vez abierta la terminal, ingresa el siguiente comando:

```bash
git clone https://github.com/skym0ds/MiniProyecto-Analizador-de-Textos
```

Es posible que te aparezca una ventana pidiendo que ingreses tu nombre de usuario o correo electrónico que tienes en GitHub y la contraseña de tu cuenta. Ingrésalas para poder continuar.

Una vez clonado el repositorio, podrás acceder a la carpeta usando.

```bash
cd MiniProyecto-Analizador-deTextos
```

Si ya tienes abierto VS CODE o algún otro editor o IDE, abre una terminal integrada para continuar; si no continua en la misma terminal de hace rato.

Ejecuta la aplicación de python desde el buscador de aplicaciones de windows o ejecutalo desde la términal, ejecutado python escribirás el siguiente comando:

```bash
import nltk; nltk.download() 
```
Se abrirá un instalador gráfico en donde puesdes escoger paquetes especificos, sin embargo, en esta ocasión instalaremos todoo, presionaremos "All" y después en download.

También necesitará tkinter, pero este ya debería venir por defecto con python.

Este último paso es importante; si no se hace tendrás un montón de errores y no podrás hacer nada.


## Ejecución

Para ejecutar el proyecto bastaría con poner el siguiente comando en la consola desde visual studio:

```bash
python analizadortext.py
```





















[Python]: https://www.python.org/downloads/
[Visual Studio Code]: https://code.visualstudio.com/
