
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

## /jobs-taked
- **GET**: Retorna la lista de los trabajos tomados por algun profesional

## /user-by-job/<JOB>
- **GET**: Retorna la lista a los profesionales en base a un trabajo espcificado

## /history
- **GET**: Retorna el historial de solicitudes de una persona o trabajador
- **NOTA**: Si eres administrador se retorna el historial de todos los usuarios

## /users/<ROL>
- **GET**: Dependiendo del rol Retorna a todos los usuarios o trabajadores
### /users/administrador
- **GET**: Retorna a todos los usuarios sin importar el rol, pero se valida que la peticion sea por un usuario administrador

## /users-filter
- **DESACTIVADO**: Retorna a todos los usuarios o trabajadores en base a un filtro

# TAREAS
- [x] Necesitamos una ruta que liste todas las ocupaciones (las profesiones)
- [x] Otra ruta que liste a todas las personas respecto a una ocupación en específico
- [x] Una ruta para login
- [x] Otra para registarse
- [ ] Un post para hacer la solicitud de un trabajador
- [x] Listar el historial de solicitudes de una persona
- [x] Listar el historial de solicitudes de un trabajador
- [x] Falta una ruta que lista a todos los usuarios

# Variable de entorno
- El archivo envEjemplo, contiene un ejemplo de la estructura del archivo .env en caso que no se quiera ejecutar la app desde el contenedor de docker