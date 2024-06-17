
# EJECUCION
- Te mueves a la ruta donde esta el archivo docker-compose.yml, y ejecutas el siguiente comando: sudo docker-compose up --build


# Endpoints

## /register/cliente
- **GET**: Retorna el token CSRF para validar el formulario. Debes almacenarlo en un encabezado llamado `X-CSRFToken`.
- **POST**: Si los datos del formulario son correctos, retorna el estado 201 y los datos almacenados. En caso de algún problema, retorna el estado 400 junto con los datos ingresados en el formulario.

## /register/trabajador
- **GET**: Retorna las labores que puede escoger el profesional a registrar y el token CSRF para validar el formulario. Debes almacenar el token en un encabezado llamado `X-CSRFToken`.
- **POST**: Si los datos del formulario son correctos, retorna el estado 201 y los datos almacenados. En caso de algún problema, retorna el estado 400 junto con los datos ingresados en el formulario.
## /register/administrador
- Este registra nuevos administradores y lo demas es lo mismo que los registers anteriores :)

### Datos a recibir de los dos register anteriores:
- A continuacion se especifica cuales son los parametros del formulario que el back espera recibir para registrar nuevos usuarios y en que rutas se espera cada uno. EL NOMBRE DEL PARAMETRO TIENE QUE SER IGUAL
- email (cliente, trabajador, administrador)
- password (cliente, trabajador, administrador)
- recibo_publico (cliente)
- name (cliente, trabajador, administrador)
- lastname (cliente, trabajador, administrador)
- latitud (cliente, trabajador)
- longitud (cliente, trabajador)
- foto_perfil (trabajador)
- imagen_documento (trabajador)
- labor (trabajador)
- precio_hora (trabajador)
- telefono (cliente, trabajador)
- tipo_tarjeta (cliente)
- codigo_seguridad (cliente)
- fecha_expiracion (cliente)
- numero_tarjeta (cliente)


## /login
- **GET**: Retorna el token CSRF para validar el formulario. Debes almacenarlo en un encabezado llamado `X-CSRFToken`.
- **POST**: Los parametros esperados son (EL NOMBRE DEL PARAMETRO TIENE QUE SER IGUAL):
  - username
  - password
  Si se usan las credenciales correctas, retorna el token de acceso JWT con el estado 200. Si las credenciales no son correctas, retorna un JSON con la clave "error" y el estado 401.
  
## /
- Si el usuario está logeado correctamente y el JWT sigue activo, retorna datos de prueba con el estado 200.
- Si no se tiene acceso (es decir, si no se cuenta con el JWT o si ha vencido), retorna un JSON con la clave "msg" y distintos estados según el error.

## /jobs/names
- **GET**: Retorna la lista de los nombres de las labores tomados por algun profesional

## /jobs/details
- **GET**: Retorna la lista de los detalles sobre las labores tomadas por algun profesional


## /labor/JOB
- **GET**: Retorna la lista a los profesionales en base a un trabajo espcificado

## /history
- **GET**: Retorna el historial de solicitudes de una persona o trabajador
- **NOTA**: Si eres administrador se retorna el historial de todos los usuarios

## /users/ROL
- **GET**: Dependiendo del rol Retorna a todos los usuarios o trabajadores
### /users/administrador
- **GET**: Retorna a todos los usuarios sin importar el rol, pero se valida que la peticion sea por un usuario administrador

## /verify/sesion
- **GET**: Verifica la validez del JWT y retorna ciertos datos dependiendo del rol de los usuarios

## /user/id



## /users-filter
- **DESACTIVADO**: Retorna a todos los usuarios o trabajadores en base a un filtro

# Variable de entorno
- El archivo envEjemplo, contiene un ejemplo de la estructura del archivo .env en caso que no se quiera ejecutar la app desde el contenedor de docker

# TAREAS
- [x] Un post para hacer la solicitud de un trabajador
- [x] Obtener calificaciones del trabajador
- [x] Retornar el rol en el post del login
- [x] Reparar login
- [x] Orden de aparicion de los trabajadores, labor/JOB, sacar promedio de estrellas

# TAREAS DEF:
- [x] Hacer una ruta de login, esta debe retornar el jwt_token y un objeto con los atributos más importantes de un usuario (nombre, apellido, telefono, rol) (para cliente también obtener la longitud y la latitud) (si es trabajador obtener su calificación de estrellas promedio) ( si es administraod, solo con el correo, la contraseña y el rol basta)
- **/login** POST
<br>

- [?] Hacer una ruta de registre en la cual se registre por un rol en específico. Para el rol de cliente este debe de pedir obligatoriamente una tarjeta de crédito (Añadir en la tabla Tarjeta y MetodoPago) 
- **ESO YA ESTA, NO?**
<br>

- [x] Hacer una ruta que verifique el estado de una jwt_token (Si aún es válida). Debe retornar la información del usuario dependiendo del rol como lo dije anteriormente en el login.
- **/verify/sesion** GET
<br>

- [x] Hacer una ruta de liste todas las labores de hay registrada en la base de datos y que tengan trabajadores disponibles (nombre, descripción, imagen, numero de trabajadores)
- **/jobs/details** GET
<br>

- [x] Hacer una ruta que liste los nombres de todas las labores que hay en la base de datos y que tengan trabajadores disponibles (SOLO EL NOMBRE EN UN ARRAY)
- **/jobs/names** GET
<br>

- [x] Hacer una ruta que obtenga la información todos lo usuarios que hacen una labor en específico y que estén disponibles (/labor/<nombre_labor>) (Traer TODA la información del trabajador e incluir su promedio de estrellas)
- **/labor/JOB** GET
<br>

- [x] Hacer una ruta que obtenga la información de UN solo trabajador en base a una labor en específico (/labor/<nombre_labor>/<id_usuario>) (Traer TODA la información del trabajador)
- **/user/ID** GET
<br>

- [x] Hacer ruta que retorne todas las solicitudes en proceso o hechas por un cliente/trabajador (/solicitud/<id_cliente> o /solicitud/<id_trabajador>) (Si es un administrador, mostrar todas las solicitudes del sistema) 
- **/solicitud/ID** GET
- **/history** GET, retorna todas las solicutudes, solo para administradores, si no es administrador retornara el historial de dicho usuario
<br>

- [x] Hacer una ruta para hacer una solicitud a un trabajador en específico (Recuerda cambiar el valor de la disponibilidad del trabajador) (Esta vuelve a retornar la información de la solicitud registrada en la base de datos) (se debe añadir el id de la tarjeta del cliente automáticamente (Solo puede tener una tarjeta))
- **/solicitud/add** POST
- Este endpoint espera un DATAFORM(**descripcion**, **trabajador_id**), y este endpoint solo funciona si el usuario es un Cliente
- Retorna los datos añadidos la clave es el nombre de las columnas de la base de datos
<br>

- [x] Hacer una ruta para calificar a un trajador por una solicitud en específico (/calificacion/<solicitud_id>) (Llamas la tablas de solicitudes y de ahí obtienes el id del cleinte y del trabajador) (en la petición se pondrán las estrellas que se pusieron y el comentario de la calificación, la fecha se pone automáticamente por la base de datos)
- **/calificacion/SOLICITUD_ID** POST
- Este endpoint espera un DATAFORM(**estrellas**, **comentario**), este endpoint solo funciona si la persona que califica es el cliente de aquella solicitud
<br>

- [x] ruta para que un trabajador pueda definir si una solicitud ya fue completada
- **/solicitud/SOLICITUD_ID** POST
<br>

- [x] ruta que retorna la calificacion y la solicitud
- **/calificacion/trabajador_id** GET

## OPCIONALES:
- [x] Hacer una ruta que obtenga la información todos lo usuarios que hacen una labor en específico y que estén disponibles y que estén cerca a una latitud y longitud específica (/labor/<nombre_labor>) (Traer TODA la información del trabajador) (Puedes usar la fórmula de la distancia Haversine para filtrar las latitudes y longitudes)
<br>
