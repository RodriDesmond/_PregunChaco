# _PregunChaco
Aplicación web tipo trivia de preguntas y respuestas. Creada en el marco de la Segunda Etapa del Informatorio 2021 por integrantes del Grupo 1 - Comisión 5.

Contiene:
* App Usuarios donde se define registro, login y logout modificado de los formularios de Django. Posibilidad de modificar, personalizar y visualizar perfil de usuario.
* App Preguntas donde se utilizan modelos para la creación y almacenamiento de preguntas y respuestas en diferentes categorías.
Cada pregunta incorpora una imagen alusiva, y un pequeño comentario didáctico ampliatorio de la respuesta correcta.
* App Trivia donde se define y ejecuta la dinámica del juego, consistente en un listado aleatorio de preguntas y sus respectivas opciones, divididas por categorias, con boton para terminar.
* App Resultado donde se define y recopila los puntajes del usuario y los muestra, como también un ranking por categoría de todos los participantes. Incorpora opción para compartir resultados.
* Perfil usuario y admin. Gestión de los datos desde el perfil de Admin de Django, almacenamiento en BDD Sqlite3.
