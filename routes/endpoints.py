from flask import Blueprint
import handlers.endpoint_handlers as handler
from handlers import handler_users, handler_sesion

api = Blueprint('api', __name__)

api.add_url_rule('/', 'landing', handler.index)

# Envia el CSRF token para validar el formulario - GET
# Recibe los datos del registro de un profesional - POST
api.add_url_rule('/register/user', 'endpoint registrar usuario', handler_users.registerUser, methods=['POST', 'GET'])
api.add_url_rule('/register/professional', 'endpoint registrar profesional', handler_users.registerProfessional, methods=['POST', 'GET'])

api.add_url_rule('/login', 'login', handler_sesion.login, methods=['POST', 'GET'])
api.add_url_rule('/logout', 'logout', handler_sesion.logout, methods=['GET'])