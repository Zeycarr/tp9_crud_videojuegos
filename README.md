\# TP N° 9: Conexión a Base de Datos en la Nube y CRUD en Python



Materia: Base de Datos 1 - IPET 247

Alumno: Lucio Sanchez



Descripción

Aplicación de consola en Python que se conecta a la base de datos `catalogo\_videojuegos` (TP07), alojada en Clever Cloud (MySQL), y permite realizar operaciones CRUD sobre la tabla `desarrolladoras`.

Requisitos

.Python 3.10 o superior

.Una base de datos MySQL (Clever Cloud)



Instalación

1\. Clonar el repositorio:



&#x20;  git clone URL\_DE\_TU\_REPO

&#x20;  cd tp9\_crud\_videojuegos



2\. Crear y activar el entorno virtual:

&#x20;  

&#x20;  python -m venv venv

&#x20;  venv\\Scripts\\activate

&#x20;  

3\. Instalar las dependencias:

&#x20;  

&#x20;  pip install -r requirements.txt

&#x20;  

4\. Copiar `.env.example` como `.env` y completarlo con los datos de conexión (están en el documento de texto entregado en Classroom):

&#x20;  

&#x20;  copy .env.example .env

&#x20;  



Uso



python conexion.py   # prueba la conexión

python main.py       # abre el menú CRUD





Operaciones

1\. Crear una desarrolladora

2\. Listar desarrolladoras

3\. Actualizar una desarrolladora

4\. Eliminar una desarrolladora (avisa si tiene videojuegos asociados)



Seguridad

Las credenciales se guardan en `.env`, que está en `.gitignore` y no se sube al repositorio.



Estructura

\- `conexion.py`: conexión a la base de datos

\- `main.py`: menú y operaciones CRUD

\- `.env.example`: plantilla de variables de entorno

\- `requirements.txt`: dependencias

