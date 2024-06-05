# Endpoints

## /register/user
- **GET**: Retorna el token CSRF para validar el formulario. Debes almacenarlo en un encabezado llamado `X-CSRFToken`.
- **POST**: Si los datos del formulario son correctos, retorna el estado 201 y los datos almacenados. En caso de algún problema, retorna el estado 400 junto con los datos ingresados en el formulario.

## /register/professional
- **GET**: Retorna las labores que puede escoger el profesional a registrar y el token CSRF para validar el formulario. Debes almacenar el token en un encabezado llamado `X-CSRFToken`.
- **POST**: Si los datos del formulario son correctos, retorna el estado 201 y los datos almacenados. En caso de algún problema, retorna el estado 400 junto con los datos ingresados en el formulario.

## /login
- **GET**: Retorna el token CSRF para validar el formulario. Debes almacenarlo en un encabezado llamado `X-CSRFToken`.
- **POST**: Las credenciales de prueba son:
  - Usuario: juan
  - Contraseña: pepito123
  Si se usan las credenciales correctas, retorna el token de acceso JWT con el estado 200. Si las credenciales no son correctas, retorna un JSON con la clave "error" y el estado 401.

## /
- Si el usuario está logeado correctamente y el JWT sigue activo, retorna datos de prueba con el estado 200.
- Si no se tiene acceso (es decir, si no se cuenta con el JWT o si ha vencido), retorna un JSON con la clave "msg" y distintos estados según el error.
