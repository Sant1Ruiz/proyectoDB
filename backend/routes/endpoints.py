from flask import Blueprint
import handlers.endpoint_handlers as handler
from handlers import handler_users, handler_sesion

api = Blueprint('api', __name__)

api.add_url_rule('/', 'landing', handler.index)

# Envia el CSRF token para validar el formulario - GET
# Recibe los datos del registro de un profesional - POST
api.add_url_rule('/register/cliente', 'endpoint registrar cliente', handler_users.registerUser, methods=['POST', 'GET'])
api.add_url_rule('/register/trabajador', 'endpoint registrar profesional', handler_users.registerProfessional, methods=['POST', 'GET'])
api.add_url_rule('/register/administrador', 'endpoint registrar administrador', handler_users.registerAdmin, methods=['POST', 'GET'])

api.add_url_rule('/login', 'login', handler_sesion.login, methods=['POST', 'GET'])
api.add_url_rule('/logout', 'logout', handler_sesion.logout, methods=['GET'])

api.add_url_rule('/jobs-taked', 'endpoint trabajos tomados', handler.list_jobs_taked, methods=['GET'])
api.add_url_rule('/user-by-job/<job>', 'endpoint user by job', handler.get_professional_for_job, methods=['GET'])
api.add_url_rule('/history', 'endpoint history', handler.list_history, methods=['GET'])
api.add_url_rule('/users/<rol>', 'endpoint users', handler.list_users, methods=['GET'])
#api.add_url_rule('/users-filter', 'endpoint users filter', handler.list_users_filter, methods=['GET'])

