Este es un proyecto de Django que utiliza la API de la NASA para mostrar la Imagen Astronómica del Día (APOD).
Este proyecto utiliza la [API de la NASA](https://api.nasa.gov/) para obtener la Imagen Astronómica del Día (APOD). Se requiere una clave de API de la NASA para acceder a la API, la cual se almacena de forma segura en el código del proyecto.
Para acceder a la API de la NASA, utilicé la biblioteca `requests` de Python para realizar solicitudes HTTP. Primero, obtuve una clave de API de la NASA registrándome en el sitio web de la API. Luego, utilicé esta clave de API para autenticar mis solicitudes a la API.
En la vista `home` de mi aplicación Django, realicé una solicitud GET al endpoint `/planetary/apod` de la API de la NASA para obtener la Imagen Astronómica del Día. Procesé la respuesta JSON y rendericé los datos en una plantilla HTML para que los usuarios pudieran ver la imagen astronómica del día en mi aplicación web.


