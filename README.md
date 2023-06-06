# Construction-helmet-detection

### Proyecto de la Pontificia Universidad Católica de Chile, enfocado a aumentar la prevención de riesgos en las obras de construcción, mediante el monitoreo del uso del casco de seguridad en los trabajadores.

El proyecto utiliza datos entrenados de detección de objetos. Estos datos son extraídos de bases de datos online públicas. Sin embargo, el archivo `full_body.xml` y `helmet.xml` son producto a un entrenamiento propio con _HAAD cascade training system_. Se utilizaron 200 imágenes positivas y 450 imágenes negativas para su entrenamiento.

El resto de data y la estrategia de reconocimiento fue extraída del siguiente link: https://core-electronics.com.au/guides/object-identify-raspberry-pi/#Down

### Funcionamiento
1. Para ejecutar el proyecto, se debe clonar el repositorio e ingresar a la carpeta __src__ .
2. Se puede correr cualquiera de los tres detectores. La diferencia principal es que cada uno puedes ingresar específicamente qué detectar. Se recomienda leer los script y utilizar el que sea del mayor agrado. Todos detectan objetos con la misma certeza. Si bien ahora mismo se puede ingresar el objeto que se quiere detectar, se debe realizar un estudio de entrenamiento mayor para conseguir una base de datos propia sobre el uso del casco de construcción. Para la ejecución: `python3 archivo.py`.

El presente proyecto es una simplificación del uso real que tendría, ya que en la práctica, sólo existirá un script que detecte el objeto __Persona__ y el objeto __Casco__ . Con este script, se detectará la presencia de una persona sin su casco, donde en cuyo caso se generará un sonido de alerta para advertir a la persona del riesgo. 

El script se incorpora a una Raspberry4 para poder captar las imágenes en tiempo real y reproducir el sonido.
