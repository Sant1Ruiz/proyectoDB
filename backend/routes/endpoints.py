from flask import Blueprint
import handlers.endpoint_handlers as handler
from handlers import handler_users, handler_sesion

api = Blueprint('api', __name__)

api.add_url_rule('/', 'landing', handler.index)

# Envia el CSRF token para validar el formulario - GET
# Recibe los datos del registro de un cliente, profesional o administrador - POST
api.add_url_rule('/register/cliente', 'endpoint registrar cliente', handler_users.registerUser, methods=['POST', 'GET'])
api.add_url_rule('/register/trabajador', 'endpoint registrar profesional', handler_users.registerProfessional, methods=['POST', 'GET'])
api.add_url_rule('/register/administrador', 'endpoint registrar administrador', handler_users.registerAdmin, methods=['POST', 'GET'])

# Envia el CSRF token para validar el formulario - GET
# Recibe los datos de inicio de sesion de los usuarios | Retorna los datos del usuario - POST
api.add_url_rule('/login', 'login', handler_sesion.login, methods=['POST', 'GET'])

# No hace nada :)
api.add_url_rule('/logout', 'logout', handler_sesion.logout, methods=['GET'])

# Retorna las labores y sus detalles, solo de las labores tomadas por al menos un trabajador - GET
api.add_url_rule('/jobs/details', 'endpoint trabajos detalles', handler.list_jobs_taked_details, methods=['GET'])
# Retorna los nombres de las labores, solo de las labores tomadas por al menos un trabajador - GET
api.add_url_rule('/jobs/names', 'endpoint trabajos nombres', handler.list_jobs_takeds_names, methods=['GET'])

# Retorna todos los usuarios y sus detalles que cumplen con la labor especificada - GET
api.add_url_rule('/labor/<job>', 'endpoint labor job', handler.get_professional_for_job, methods=['GET'])

# Retorna los datos de solicitudes del usuario que hizo la peticion - GET
# Si es administrador retorna todas las solicitudes
api.add_url_rule('/history', 'endpoint history', handler.list_history, methods=['GET'])

# Retorna una lista de usuarios dependiendo de su rol - GET
api.add_url_rule('/users/<rol>', 'endpoint users', handler.list_users, methods=['GET'])

# Valida el JWT y retorna la informacion del usuario - GET
api.add_url_rule('/verify/sesion', 'endpoint verify', handler_sesion.verify_sesion, methods=['GET'])

# Retorna la informacion de un solo trabajador - GET
api.add_url_rule('/user/<id>', 'endpoint user', handler.get_user_details, methods=['GET'])

# Retorna todas las solicitudes de un cliente o trabajador, si es admin se usa history - GET
api.add_url_rule('/solicitud/<id>', 'endpoint solicitud', handler.get_solicitud, methods=['GET', 'POST'])

# Genera una nueva solicitud y retorna todos los datos creados - POST
api.add_url_rule('/solicitud/add', 'endpoint añadir solicitud', handler.generate_solictud, methods=['POST'])

# Califica una solicitud - POST
api.add_url_rule('/calificacion/<solicitud_id>', 'endpoint añadir calificaciones', handler.add_calificacion, methods=['POST'])